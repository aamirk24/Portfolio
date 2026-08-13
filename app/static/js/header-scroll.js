(() => {
  const header = document.querySelector("[data-site-header]");
  if (!header) return;

  const movementThreshold = 8;
  let previousPosition = Math.max(window.scrollY, 0);
  let ticking = false;

  const updateHeader = () => {
    const currentPosition = Math.max(window.scrollY, 0);
    const movement = currentPosition - previousPosition;
    const menuIsOpen = Boolean(header.querySelector(".navbar-collapse.show"));
    const headerHasFocus = header.contains(document.activeElement);

    if (currentPosition <= 24 || menuIsOpen || headerHasFocus) {
      header.classList.remove("is-hidden");
    } else if (movement > movementThreshold) {
      header.classList.add("is-hidden");
    } else if (movement < -movementThreshold) {
      header.classList.remove("is-hidden");
    }

    if (Math.abs(movement) > movementThreshold || currentPosition <= 24) {
      previousPosition = currentPosition;
    }
    ticking = false;
  };

  window.addEventListener("scroll", () => {
    if (!ticking) {
      window.requestAnimationFrame(updateHeader);
      ticking = true;
    }
  }, { passive: true });

  header.addEventListener("focusin", () => header.classList.remove("is-hidden"));
  header.addEventListener("show.bs.collapse", () => header.classList.remove("is-hidden"));
})();
