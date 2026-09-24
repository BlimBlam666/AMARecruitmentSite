(() => {
  const nav = document.querySelector(".primary-nav");
  const toggle = document.querySelector(".nav-toggle");

  if (nav && toggle) {
    const closeNav = () => {
      nav.dataset.open = "false";
      toggle.setAttribute("aria-expanded", "false");
    };

    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") === "true";
      nav.dataset.open = open ? "false" : "true";
      toggle.setAttribute("aria-expanded", String(!open));
    });

    nav.addEventListener("click", (event) => {
      if (event.target.closest("a")) closeNav();
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeNav();
        toggle.focus();
      }
    });

    window.matchMedia("(min-width: 48rem)").addEventListener("change", (event) => {
      if (event.matches) closeNav();
    });
  }

  document.querySelectorAll("[data-current-year]").forEach((node) => {
    node.textContent = String(new Date().getFullYear());
  });
})();
