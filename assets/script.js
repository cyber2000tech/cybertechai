/* Cyber Tech | progressive enhancement. No dependencies or build step. */
(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const year = document.getElementById('copyright-year');
  if (year) year.textContent = new Date().getFullYear();
  const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const reduceMotion = motionPreference.matches;
  const header = document.querySelector('.site-header');
  const menuButton = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav-links');

  function updateHeader() {
    header?.classList.toggle('is-scrolled', window.scrollY > 18);
  }
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  function closeMenu() {
    nav?.classList.remove('is-open');
    menuButton?.setAttribute('aria-expanded', 'false');
    menuButton?.setAttribute('aria-label', 'Open navigation');
  }
  menuButton?.addEventListener('click', () => {
    const open = !nav.classList.contains('is-open');
    nav.classList.toggle('is-open', open);
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && nav?.classList.contains('is-open')) { closeMenu(); menuButton?.focus(); } });
  document.addEventListener('click', e => {
    if (nav?.classList.contains('is-open') && !header.contains(e.target)) closeMenu();
  });
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  window.addEventListener('resize', () => { if (window.innerWidth > 900) closeMenu(); });

  // Only elements marked .reveal animate; ordinary content remains readable without JS.
  if (!reduceMotion && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      }
    }, { threshold: 0.10, rootMargin: '0px 0px -30px 0px' });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('is-visible'));
  }

  // Fade between local HTML pages. External links, hash jumps and modified clicks stay native.
  if (!reduceMotion) {
    document.addEventListener('click', event => {
      const anchor = event.target.closest('a[href]');
      if (!anchor || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || anchor.hasAttribute('download') || anchor.target === '_blank') return;
      const next = new URL(anchor.href, window.location.href);
      const here = new URL(window.location.href);
      if (next.protocol !== here.protocol || next.host !== here.host || !next.pathname.endsWith('.html') && !next.pathname.endsWith('/')) return;
      if (next.pathname === here.pathname) return;
      event.preventDefault();
      document.body.classList.add('is-leaving');
      window.setTimeout(() => { window.location.assign(next.href); }, 185);
    });
    window.addEventListener('pageshow', () => document.body.classList.remove('is-leaving'));
  }

  // Subtle depth response for precise desktop pointers only. Touch screens retain
  // the same continuously animated SVG orbits without costly pointer tracking.
  const hero = document.querySelector('.home-hero');
  const orbSide = document.querySelector('.hero-side');
  const canParallax = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (hero && orbSide && canParallax && !reduceMotion) {
    let pointerFrame = 0;
    let px = 0, py = 0;
    hero.addEventListener('pointermove', event => {
      const rect = hero.getBoundingClientRect();
      px = (event.clientX - rect.left) / Math.max(1, rect.width) - .5;
      py = (event.clientY - rect.top) / Math.max(1, rect.height) - .5;
      if (pointerFrame) return;
      pointerFrame = window.requestAnimationFrame(() => {
        pointerFrame = 0;
        orbSide.style.setProperty('--orbit-x', (px * 13).toFixed(1) + 'px');
        orbSide.style.setProperty('--orbit-y', (py * 11).toFixed(1) + 'px');
      });
    }, { passive: true });
    hero.addEventListener('pointerleave', () => {
      orbSide.style.setProperty('--orbit-x', '0px');
      orbSide.style.setProperty('--orbit-y', '0px');
    });
  }

  // Lightweight starfield stays animated on phones and tablets, too.
  // Frames are capped and drawing sleeps while the hero is off-screen or the tab is hidden.
  const canvas = document.getElementById('starfield');
  if (canvas) {
    const ctx = canvas.getContext('2d', { alpha: true });
    if (ctx) {
      const mobile = window.matchMedia('(pointer: coarse)').matches;
      const frameInterval = mobile ? 1000 / 30 : 1000 / 40;
      let width = 0, height = 0, points = [];
      let frame = null, lastPaint = 0;
      let heroVisible = true;
      const motion = !reduceMotion;

      function draw(time) {
        ctx.clearRect(0, 0, width, height);
        for (const p of points) {
          const shimmer = motion ? .8 + .2 * Math.sin(time * .0005 * p.rate + p.phase) : 1;
          ctx.beginPath();
          ctx.fillStyle = `rgba(155, 218, 248, ${p.a * shimmer})`;
          ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      function init() {
        const box = canvas.getBoundingClientRect();
        // Capping backing resolution keeps mobile GPUs and high-DPI iPads responsive.
        const ratio = Math.min(window.devicePixelRatio || 1, mobile ? 1.5 : 2);
        width = Math.max(1, Math.round(box.width));
        height = Math.max(1, Math.round(box.height));
        canvas.width = Math.round(width * ratio);
        canvas.height = Math.round(height * ratio);
        ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
        const count = Math.min(mobile ? 48 : 66, Math.max(24, Math.round(width * height / 15000)));
        let seed = 99173;
        const random = () => ((seed = (seed * 1664525 + 1013904223) >>> 0) / 4294967296);
        points = Array.from({ length: count }, () => ({
          x: random() * width, y: random() * height,
          r: .45 + random() * 1.25, a: .15 + random() * .43,
          phase: random() * Math.PI * 2, rate: .5 + random()
        }));
        draw(0);
      }

      function stop() {
        if (frame !== null) window.cancelAnimationFrame(frame);
        frame = null;
      }
      function tick(time) {
        frame = null;
        if (!heroVisible || document.hidden) return;
        if (time - lastPaint >= frameInterval) {
          draw(time);
          lastPaint = time;
        }
        frame = window.requestAnimationFrame(tick);
      }
      function resume() {
        if (motion && heroVisible && !document.hidden && frame === null) {
          lastPaint = 0;
          frame = window.requestAnimationFrame(tick);
        }
      }

      init();
      if ('IntersectionObserver' in window) {
        const heroObserver = new IntersectionObserver(entries => {
          heroVisible = entries[0].isIntersecting;
          if (heroVisible) resume(); else stop();
        }, { threshold: 0 });
        heroObserver.observe(canvas);
      }
      document.addEventListener('visibilitychange', () => { if (document.hidden) stop(); else resume(); });
      let resizeTimer;
      window.addEventListener('resize', () => {
        window.clearTimeout(resizeTimer);
        resizeTimer = window.setTimeout(init, 130);
      }, { passive: true });
      resume();
    }
  }
})();
