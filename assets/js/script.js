(() => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Promo bar ---------- */
  const promoBar = document.getElementById('promoBar');
  const promoClose = document.getElementById('promoClose');
  if (promoBar && promoClose) {
    try {
      if (sessionStorage.getItem('promoDismissed') === '1') {
        promoBar.classList.add('dismissed');
      }
    } catch (e) { /* sessionStorage unavailable */ }

    promoClose.addEventListener('click', () => {
      promoBar.classList.add('dismissed');
      try { sessionStorage.setItem('promoDismissed', '1'); } catch (e) { /* ignore */ }
    });
  }

  /* ---------- Footer year ---------- */
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- Header scroll state ---------- */
  const header = document.getElementById('siteHeader');
  const onScroll = () => {
    if (window.scrollY > 20) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- Mobile menu ---------- */
  const menuToggle = document.getElementById('menuToggle');
  const mainNav = document.getElementById('mainNav');
  menuToggle.addEventListener('click', () => {
    const isOpen = mainNav.classList.toggle('open');
    menuToggle.classList.toggle('open', isOpen);
    menuToggle.setAttribute('aria-expanded', String(isOpen));
  });
  mainNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mainNav.classList.remove('open');
      menuToggle.classList.remove('open');
      menuToggle.setAttribute('aria-expanded', 'false');
    });
  });

  /* ---------- Scroll reveal ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  if (prefersReducedMotion) {
    revealEls.forEach(el => el.classList.add('in-view'));
  } else {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(el => revealObserver.observe(el));
  }

  /* ---------- Rotating hero text ---------- */
  const rotatingWords = ['para vender mais.', 'para crescer rápido.', 'para automatizar tarefas.', 'para se destacar online.'];
  const rotatingEl = document.getElementById('rotatingText');
  if (rotatingEl && !prefersReducedMotion) {
    let idx = 0;
    setInterval(() => {
      idx = (idx + 1) % rotatingWords.length;
      rotatingEl.style.opacity = '0';
      rotatingEl.style.transform = 'translateY(6px)';
      setTimeout(() => {
        rotatingEl.textContent = rotatingWords[idx];
        rotatingEl.style.opacity = '1';
        rotatingEl.style.transform = 'translateY(0)';
      }, 260);
    }, 2800);
    rotatingEl.style.transition = 'opacity 0.26s ease, transform 0.26s ease';
    rotatingEl.style.display = 'inline-block';
  }

  /* ---------- Animated stat counters ---------- */
  const statEls = document.querySelectorAll('.stat-num');
  const animateCount = (el) => {
    const target = parseInt(el.dataset.target, 10) || 0;
    const duration = 1400;
    const start = performance.now();
    const step = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target);
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if (statEls.length) {
    if (prefersReducedMotion) {
      statEls.forEach(el => { el.textContent = el.dataset.target; });
    } else {
      const statObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            statObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });
      statEls.forEach(el => statObserver.observe(el));
    }
  }

  /* ---------- Tilt effect on cards ---------- */
  if (!prefersReducedMotion && window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.tilt-card').forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `perspective(700px) rotateX(${(-y * 6).toFixed(2)}deg) rotateY(${(x * 6).toFixed(2)}deg) translateY(-4px)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(700px) rotateX(0) rotateY(0) translateY(0)';
      });
    });

    /* ---------- Cursor glow ---------- */
    const glow = document.querySelector('.cursor-glow');
    let glowX = window.innerWidth / 2;
    let glowY = window.innerHeight / 2;
    let targetX = glowX;
    let targetY = glowY;
    window.addEventListener('mousemove', (e) => {
      targetX = e.clientX;
      targetY = e.clientY;
    });
    const animateGlow = () => {
      glowX += (targetX - glowX) * 0.12;
      glowY += (targetY - glowY) * 0.12;
      if (glow) glow.style.transform = `translate(${glowX}px, ${glowY}px) translate(-50%, -50%)`;
      requestAnimationFrame(animateGlow);
    };
    requestAnimationFrame(animateGlow);
  }

  /* ---------- Background music toggle ---------- */
  const bgMusic = document.getElementById('bgMusic');
  const musicToggle = document.getElementById('musicToggle');
  if (bgMusic && musicToggle) {
    bgMusic.volume = 0.35;

    const disableMusic = () => {
      bgMusic.pause();
      musicToggle.disabled = true;
      musicToggle.classList.remove('playing');
      musicToggle.title = 'Adicione o arquivo assets/audio/background.mp3 para ativar a música';
      musicToggle.setAttribute('aria-label', 'Música de fundo indisponível');
    };

    bgMusic.addEventListener('error', disableMusic);

    // 'playing' fires only once real playback starts — the reliable signal that the source works.
    bgMusic.addEventListener('playing', () => {
      musicToggle.classList.add('playing');
      musicToggle.setAttribute('aria-pressed', 'true');
      musicToggle.setAttribute('aria-label', 'Pausar música de fundo');
    });

    musicToggle.addEventListener('click', () => {
      if (bgMusic.paused) {
        bgMusic.play().catch(disableMusic);
      } else {
        bgMusic.pause();
        musicToggle.classList.remove('playing');
        musicToggle.setAttribute('aria-pressed', 'false');
        musicToggle.setAttribute('aria-label', 'Ativar música de fundo');
      }
    });

    // Try to autoplay on load. Most browsers block unmuted autoplay without a user
    // gesture, so fall back to starting on the visitor's first interaction with the page.
    const attemptAutoplay = () => bgMusic.play().catch(() => {
      const startOnFirstInteraction = () => {
        bgMusic.play().catch(() => {});
        ['pointerdown', 'keydown', 'scroll', 'touchstart'].forEach(evt =>
          document.removeEventListener(evt, startOnFirstInteraction)
        );
      };
      ['pointerdown', 'keydown', 'scroll', 'touchstart'].forEach(evt =>
        document.addEventListener(evt, startOnFirstInteraction, { once: true, passive: true })
      );
    });
    attemptAutoplay();
  }

  /* ---------- Hero particle network ---------- */
  const canvas = document.getElementById('particles');
  if (canvas && !prefersReducedMotion) {
    const ctx = canvas.getContext('2d');
    const heroSection = canvas.closest('.hero');
    let particles = [];
    let width = 0, height = 0, dpr = Math.min(window.devicePixelRatio || 1, 2);

    const colors = ['rgba(138, 63, 252, 0.8)', 'rgba(0, 240, 255, 0.8)', 'rgba(255, 61, 203, 0.7)'];

    const resize = () => {
      const rect = heroSection.getBoundingClientRect();
      width = rect.width;
      height = rect.height;
      canvas.width = width * dpr;
      canvas.height = height * dpr;
      canvas.style.width = width + 'px';
      canvas.style.height = height + 'px';
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      const count = Math.min(70, Math.round((width * height) / 18000));
      particles = Array.from({ length: count }, () => ({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35,
        r: Math.random() * 1.6 + 0.6,
        color: colors[Math.floor(Math.random() * colors.length)]
      }));
    };

    const step = () => {
      ctx.clearRect(0, 0, width, height);

      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0 || p.x > width) p.vx *= -1;
        if (p.y < 0 || p.y > height) p.vy *= -1;
      });

      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const a = particles[i], b = particles[j];
          const dx = a.x - b.x, dy = a.y - b.y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 120) {
            ctx.strokeStyle = `rgba(255,255,255,${0.08 * (1 - dist / 120)})`;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(a.x, a.y);
            ctx.lineTo(b.x, b.y);
            ctx.stroke();
          }
        }
      }

      particles.forEach(p => {
        ctx.beginPath();
        ctx.fillStyle = p.color;
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
      });

      requestAnimationFrame(step);
    };

    resize();
    requestAnimationFrame(step);
    window.addEventListener('resize', resize, { passive: true });
  }

  /* ---------- Contact form (front-end only placeholder) ---------- */
  const form = document.getElementById('contactForm');
  const formNote = document.getElementById('formNote');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      formNote.textContent = 'Mensagem pronta! Conecte este formulário a um serviço de envio (ex: Formspree, EmailJS) ou ao seu back-end para receber os contatos.';
    });
  }
})();
