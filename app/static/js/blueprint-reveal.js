(() => {
  const hero = document.querySelector(".hero");
  const field = document.querySelector("[data-blueprint-field]");
  if (!hero || !field) return;

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (reduceMotion.matches) {
    hero.classList.add("blueprint-ready");
    return;
  }

  window.requestAnimationFrame(() => hero.classList.add("blueprint-ready"));

  const rotator = hero.querySelector("[data-headline-rotator]");
  const words = rotator ? [...rotator.querySelectorAll(".kinetic-word")] : [];
  let activeWord = 0;

  if (words.length > 1) {
    window.setInterval(() => {
      if (document.hidden) return;
      const outgoing = words[activeWord];
      activeWord = (activeWord + 1) % words.length;
      const incoming = words[activeWord];

      outgoing.classList.remove("is-active");
      outgoing.classList.add("is-exiting");
      incoming.classList.add("is-active");

      window.setTimeout(() => outgoing.classList.remove("is-exiting"), 700);
    }, 2800);
  }

})();
