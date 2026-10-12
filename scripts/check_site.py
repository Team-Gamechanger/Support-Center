"""Check the built wiki, its legacy URLs and the main support journeys.

Run after `mkdocs build --strict`, from the repository root.
"""

from collections import Counter, deque
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit

from bs4 import BeautifulSoup
from mkdocs.config import load_config


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ORIGIN = "https://support.jackboxpatch.de/"


def main():
    errors = []
    pages = {
        path.relative_to(SITE).as_posix(): BeautifulSoup(
            path.read_text(encoding="utf-8"), "html.parser"
        )
        for path in SITE.rglob("*.html")
    }
    if "index.html" not in pages:
        raise SystemExit("No build found. Run mkdocs build --strict first.")

    def resolve(source, href):
        source_url = source.removesuffix("index.html") if source.endswith("index.html") else source
        url = urlsplit(urljoin(ORIGIN + source_url, href))
        if url.scheme not in {"http", "https"} or url.netloc != urlsplit(ORIGIN).netloc:
            return None
        path = unquote(url.path).lstrip("/")
        if not path or path.endswith("/"):
            path += "index.html"
        return path, unquote(url.fragment)

    graph = {}
    for source, soup in pages.items():
        ids = [node["id"] for node in soup.select("[id]")]
        for key, count in Counter(ids).items():
            if count > 1:
                errors.append(f"Duplicate id: {source}#{key}")
        # Validate generated navigation as well as article links, scripts and images.
        for node in soup.select("a[href], img[src], script[src], link[href]"):
            if node.name == "link" and "canonical" in node.get("rel", []):
                continue
            href = node.get("href", node.get("src", ""))
            target = resolve(source, href)
            if target is None:
                continue
            path, fragment = target
            if not (SITE / path).is_file():
                errors.append(f"Missing target: {source} -> {href}")
            elif fragment and path in pages and not pages[path].find(id=fragment):
                errors.append(f"Missing anchor: {source} -> {href}")
        article = soup.select_one("article")
        if article:
            graph[source] = {
                target[0]
                for a in article.select("a[href]")
                if (target := resolve(source, a["href"])) and target[0] in pages
            }

    redirects = {}
    for source, soup in pages.items():
        refresh = soup.find("meta", attrs={"http-equiv": "refresh"})
        if refresh:
            href = refresh["content"].split("url=", 1)[1].strip()
            target = resolve(source, href)
            if target is None or target[0] not in pages:
                errors.append(f"Invalid redirect: {source} -> {href}")
            else:
                redirects[source] = target[0]

    legacy = json.loads((ROOT / "tests/legacy-anchors.json").read_text(encoding="utf-8"))
    for source, anchors in legacy.items():
        if source not in pages:
            errors.append(f"Legacy URL missing: {source}")
            continue
        destination = source
        visited = set()
        while destination in redirects and destination not in visited:
            visited.add(destination)
            destination = redirects[destination]
        if destination in visited:
            errors.append(f"Redirect cycle: {source}")
        for anchor in anchors:
            if not pages[destination].find(id=anchor):
                errors.append(f"Legacy anchor missing: {source}#{anchor}")

    config = load_config(str(ROOT / "mkdocs.yml"))

    def nav_paths(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, list):
            for item in value:
                yield from nav_paths(item)
        elif isinstance(value, dict):
            for item in value.values():
                yield from nav_paths(item)

    nav = Counter(nav_paths(config.nav))
    sources = {
        path.relative_to(ROOT / "docs").as_posix()
        for path in (ROOT / "docs").rglob("*.md")
        if not {"venv", ".venv"}.intersection(path.relative_to(ROOT / "docs").parts)
    }
    for source in sources | nav.keys():
        if source not in sources or nav[source] != 1:
            errors.append(f"Expected one navigation entry: {source} (found {nav[source]})")
    if any((SITE / name).exists() for name in ("venv", ".venv")):
        errors.append("A Python environment was included in the build")
    if (SITE / "CNAME").read_text(encoding="utf-8").strip() != "support.jackboxpatch.de":
        errors.append("CNAME missing or incorrect")

    distances = {"index.html": 0}
    queue = deque(distances)
    while queue:
        source = queue.popleft()
        for target in graph.get(source, set()):
            if target not in distances:
                distances[target] = distances[source] + 1
                queue.append(target)
    journeys = [
        "Installation/Windows/index.html",
        "Installation/macOS/index.html",
        "Installation/JackboxUtility/index.html",
        "Spiele/trivia-murder-party-3/index.html",
        "Wissenswertes/BugReport/index.html",
        "Deinstallation/index.html",
        "Problembehebung/index.html",
        "Problembehebung/SpielStartetNicht/index.html",
        "Problembehebung/UnvollstaendigeUebersetzung/index.html",
        "Problembehebung/JackboxUtility/index.html",
        "Problembehebung/MacOSFehlermeldung/index.html",
    ]
    for target in journeys:
        if distances.get(target, 999) > 2:
            errors.append(f"More than two article-link clicks to {target}")

    search = json.loads((SITE / "search/search_index.json").read_text(encoding="utf-8"))
    for query, target in [
        ("Steam Deck", "Installation/JackboxUtility/"),
        ("Mac", "Installation/macOS/"),
        ("englisch", "Problembehebung/UnvollstaendigeUebersetzung/"),
        ("Update", "Installation/aktualisieren/"),
        ("deinstallieren", "Deinstallation/"),
        ("HandshakeException", "Problembehebung/JackboxUtility/"),
        ("VCRUNTIME", "Problembehebung/JackboxUtility/"),
    ]:
        if not any(
            entry["location"].startswith(target)
            and query.casefold() in (entry["title"] + " " + entry["text"]).casefold()
            for entry in search["docs"]
        ):
            errors.append(f"Search index missing {query!r} for {target}")

    spoiler = pages["Wissenswertes/YDKJ/index.html"].find(id="welche-gast-moderatoren-kommen-im-spiel-vor")
    details = spoiler.find_parent("details") if spoiler else None
    if details is None or details.has_attr("open"):
        errors.append("YDKJ spoilers must start inside a closed details element")

    if errors:
        print("\n".join(errors))
        return 1
    print(
        f"OK: {len(sources)} articles, {len(legacy)} legacy URLs, "
        f"{sum(map(len, legacy.values()))} legacy heading anchors; "
        f"{len(redirects)} redirects; internal links/assets, unique navigation, two-click journeys, "
        "search content and spoiler disclosure verified."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
