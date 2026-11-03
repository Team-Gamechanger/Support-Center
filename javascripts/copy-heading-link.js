// Event delegation also covers pages loaded by Material's instant navigation.
(() => {
    const label = "Link zu diesem Abschnitt kopieren";

    function labelLinks() {
        document.querySelectorAll(".headerlink").forEach(link => {
            link.setAttribute("aria-label", label);
        });
    }

    labelLinks();
    if (typeof document$ !== "undefined") {
        document$.subscribe(labelLinks);
    }

    document.addEventListener("click", async event => {
        const link = event.target.closest(".headerlink");
        if (!link || event.button !== 0 || event.ctrlKey || event.metaKey ||
            event.shiftKey || event.altKey) return;

        event.preventDefault();
        const url = link.href;
        try {
            await navigator.clipboard.writeText(url);
        } catch {
            // Allow manual copying when clipboard access is unavailable or denied.
            window.prompt("Link zu diesem Abschnitt kopieren:", url);
        }
    });
})();
