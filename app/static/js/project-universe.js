import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.179.1/build/three.module.min.js";

(() => {
  const universe = document.querySelector("[data-project-universe]");
  const canvas = universe?.querySelector("[data-universe-canvas]");
  const labels = universe ? [...universe.querySelectorAll("[data-universe-node]")] : [];

  if (!universe || !canvas || !labels.length || !window.WebGLRenderingContext) return;

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const coarsePointer = window.matchMedia("(hover: none), (pointer: coarse)");
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  const raycaster = new THREE.Raycaster();
  const pointer = new THREE.Vector2(2, 2);
  const targetRotation = new THREE.Vector2();
  const clock = new THREE.Clock();
  const system = new THREE.Group();
  const satellites = [];
  const hitTargets = [];
  let activeIndex = -1;
  let armedIndex = -1;
  let labelHasFocus = false;

  const desktopPositions = [
    [-3.5, 1.65, 0.15],
    [-0.8, 2.2, -0.65],
    [2.75, 1.55, 0.3],
    [-3.1, -1.35, -0.5],
    [-0.05, -1.85, 0.2],
    [3.35, -1.2, -0.8],
  ];
  const tabletPositions = [
    [-3.25, 2.15, 0.1],
    [0, 2.65, -0.55],
    [3.25, 2.05, 0.2],
    [-3.25, -2.05, -0.4],
    [0, -2.6, 0.15],
    [3.25, -2, -0.6],
  ];
  const mobilePositions = [
    [-1.25, 2.85, 0.1],
    [1.25, 2, -0.45],
    [-1.25, 1, 0.15],
    [1.25, -0.15, -0.35],
    [-1.25, -1.35, 0.1],
    [1.25, -2.45, -0.5],
  ];

  scene.add(system);
  scene.add(new THREE.AmbientLight(0x9bb0ff, 1.2));
  const keyLight = new THREE.PointLight(0x5f83ff, 18, 18);
  keyLight.position.set(1.5, 2.5, 4);
  scene.add(keyLight);
  camera.position.set(0, 0, 9.6);

  const centralCore = new THREE.Mesh(
    new THREE.IcosahedronGeometry(0.34, 2),
    new THREE.MeshStandardMaterial({
      color: 0x2457f5,
      emissive: 0x102a80,
      emissiveIntensity: 1.8,
      metalness: 0.55,
      roughness: 0.18,
      flatShading: true,
    })
  );
  system.add(centralCore);

  const centralShell = new THREE.Mesh(
    new THREE.IcosahedronGeometry(0.58, 1),
    new THREE.MeshBasicMaterial({ color: 0x8ca8ff, wireframe: true, transparent: true, opacity: 0.32 })
  );
  system.add(centralShell);

  desktopPositions.forEach((position, index) => {
    const satellite = new THREE.Group();
    satellite.position.set(...position);
    satellite.userData.index = index;

    const core = new THREE.Mesh(
      new THREE.SphereGeometry(0.22, 24, 24),
      new THREE.MeshStandardMaterial({
        color: 0x2f62ff,
        emissive: 0x163bba,
        emissiveIntensity: 1.55,
        metalness: 0.68,
        roughness: 0.16,
      })
    );
    core.userData.index = index;
    satellite.add(core);
    hitTargets.push(core);

    const shell = new THREE.Mesh(
      new THREE.IcosahedronGeometry(0.31, 1),
      new THREE.MeshBasicMaterial({ color: 0xa7baff, wireframe: true, transparent: true, opacity: 0.78 })
    );
    satellite.add(shell);

    const control = satellite.position.clone().multiplyScalar(0.5);
    control.z += index % 2 === 0 ? 0.65 : -0.55;
    const curve = new THREE.QuadraticBezierCurve3(new THREE.Vector3(), control, satellite.position.clone());
    const path = new THREE.Line(
      new THREE.BufferGeometry().setFromPoints(curve.getPoints(32)),
      new THREE.LineBasicMaterial({ color: 0x557cff, transparent: true, opacity: 0.3 })
    );
    system.add(path);
    satellites.push({ group: satellite, core, shell, path });
    system.add(satellite);
  });

  const particlePositions = new Float32Array(320 * 3);
  for (let index = 0; index < particlePositions.length; index += 3) {
    const radius = 2.5 + Math.random() * 4.2;
    const angle = Math.random() * Math.PI * 2;
    particlePositions[index] = Math.cos(angle) * radius;
    particlePositions[index + 1] = (Math.random() - 0.5) * 6.2;
    particlePositions[index + 2] = Math.sin(angle) * radius - 1.4;
  }
  const particleGeometry = new THREE.BufferGeometry();
  particleGeometry.setAttribute("position", new THREE.BufferAttribute(particlePositions, 3));
  const particles = new THREE.Points(
    particleGeometry,
    new THREE.PointsMaterial({ color: 0x7897ff, size: 0.03, transparent: true, opacity: 0.62 })
  );
  system.add(particles);

  const setActiveNode = (index = -1) => {
    if (activeIndex === index) return;
    activeIndex = index;
    universe.classList.toggle("has-active-node", index >= 0);
    labels.forEach((label, labelIndex) => label.classList.toggle("is-active", labelIndex === index));
  };

  const applyResponsiveLayout = () => {
    const width = universe.clientWidth;
    const layout = width < 600 ? mobilePositions : width < 1000 ? tabletPositions : desktopPositions;
    camera.position.z = width < 600 ? 11.6 : width < 1000 ? 10.5 : 9.6;

    satellites.forEach((satellite, index) => {
      satellite.group.position.set(...layout[index]);
      const control = satellite.group.position.clone().multiplyScalar(0.5);
      control.z += index % 2 === 0 ? 0.55 : -0.45;
      const curve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(),
        control,
        satellite.group.position.clone()
      );
      satellite.path.geometry.dispose();
      satellite.path.geometry = new THREE.BufferGeometry().setFromPoints(curve.getPoints(32));
    });
  };

  const updateLabels = () => {
    const width = universe.clientWidth;
    const height = universe.clientHeight;

    satellites.forEach((satellite, index) => {
      const projected = satellite.group.getWorldPosition(new THREE.Vector3()).project(camera);
      const label = labels[index];
      const panelWidth = label.offsetWidth;
      const panelHeight = label.offsetHeight;
      const bottomClearance = index === activeIndex ? 112 : 34;
      const forceRight = index === 2 || index === 5;
      const placeLeft = projected.x > 0.32 && !forceRight;
      label.classList.toggle("is-left", placeLeft);

      let x = (projected.x * 0.5 + 0.5) * width;
      let y = (-projected.y * 0.5 + 0.5) * height;
      x = placeLeft
        ? THREE.MathUtils.clamp(x, panelWidth + 34, width - 28)
        : THREE.MathUtils.clamp(x, 28, width - panelWidth - 34);
      y = THREE.MathUtils.clamp(
        y,
        panelHeight / 2 + 24,
        height - panelHeight / 2 - bottomClearance
      );

      label.style.left = `${x}px`;
      label.style.top = `${y}px`;
      label.style.opacity = projected.z < 1 ? "1" : "0";
    });
  };

  const resize = () => {
    const width = universe.clientWidth;
    const height = universe.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.75));
    renderer.setSize(width, height, false);
    applyResponsiveLayout();
  };

  const updatePointer = (event) => {
    const bounds = canvas.getBoundingClientRect();
    pointer.x = ((event.clientX - bounds.left) / bounds.width) * 2 - 1;
    pointer.y = -((event.clientY - bounds.top) / bounds.height) * 2 + 1;
    targetRotation.y = pointer.x * 0.13;
    targetRotation.x = -pointer.y * 0.075;
  };

  const pickNode = () => {
    raycaster.setFromCamera(pointer, camera);
    const hit = raycaster.intersectObjects(hitTargets)[0];
    if (!labelHasFocus) setActiveNode(hit ? hit.object.userData.index : -1);
    canvas.style.cursor = hit ? "pointer" : "crosshair";
    return hit;
  };

  const render = () => {
    const elapsed = clock.getElapsedTime();
    if (!reduceMotion.matches) {
      system.rotation.x += (targetRotation.x - system.rotation.x) * 0.022;
      system.rotation.y += (targetRotation.y - system.rotation.y) * 0.022;
      centralCore.rotation.x = elapsed * 0.13;
      centralCore.rotation.y = elapsed * 0.2;
      centralShell.rotation.x = -elapsed * 0.08;
      centralShell.rotation.y = elapsed * 0.11;
      particles.rotation.y = elapsed * 0.01;
    }

    satellites.forEach((satellite, index) => {
      const active = index === activeIndex;
      const scale = active ? 1.7 : 1;
      satellite.group.scale.lerp(new THREE.Vector3(scale, scale, scale), reduceMotion.matches ? 1 : 0.085);
      satellite.shell.rotation.x += reduceMotion.matches ? 0 : 0.003 + index * 0.0002;
      satellite.shell.rotation.y += reduceMotion.matches ? 0 : 0.004;
      satellite.core.material.emissiveIntensity += ((active ? 2.8 : 1.25) - satellite.core.material.emissiveIntensity) * 0.08;
    });

    pickNode();
    updateLabels();
    renderer.render(scene, camera);
    window.requestAnimationFrame(render);
  };

  labels.forEach((label, index) => {
    const activate = () => {
      labelHasFocus = true;
      setActiveNode(index);
    };
    const deactivate = () => {
      labelHasFocus = false;
      setActiveNode(-1);
    };
    label.addEventListener("mouseenter", activate);
    label.addEventListener("mouseleave", deactivate);
    label.addEventListener("focus", activate);
    label.addEventListener("blur", deactivate);
    label.addEventListener("click", (event) => {
      if (coarsePointer.matches && armedIndex !== index) {
        event.preventDefault();
        armedIndex = index;
        activate();
      }
    });
  });

  canvas.addEventListener("pointermove", updatePointer);
  canvas.addEventListener("pointerleave", () => {
    pointer.set(2, 2);
    targetRotation.set(0, 0);
    setActiveNode(-1);
  });
  canvas.addEventListener("click", () => {
    const hit = pickNode();
    if (!hit) return;
    const index = hit.object.userData.index;
    if (coarsePointer.matches && armedIndex !== index) {
      armedIndex = index;
      setActiveNode(index);
      return;
    }
    window.location.assign(labels[index].href);
  });
  window.addEventListener("resize", resize);

  universe.classList.add("is-ready");
  resize();
  render();
})();
