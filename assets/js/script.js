(() => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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

  /* ---------- Service card lift on hover ---------- */
  if (!prefersReducedMotion && window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.service-card').forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `translateY(-4px) rotateX(${(-y * 4).toFixed(2)}deg) rotateY(${(x * 4).toFixed(2)}deg)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = '';
      });
    });
  }

  /* ---------- Hero orbit icons ---------- */
  const HERO_ICONS_OUTER = [
    '<path d="M5 12a11 11 0 0 1 14 0"/><path d="M8.2 15.5a6.5 6.5 0 0 1 7.6 0"/><circle cx="12" cy="19" r="1.4" fill="#fff" stroke="none"/>',
    '<path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5c-1.35 0-2.61-.32-3.73-.9L4 21l1.9-4.77A8.5 8.5 0 1 1 21 11.5Z"/>',
    '<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/>',
    '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    '<path d="M9 2v4M15 2v4M6 8h12M6 16l2 2-2 2M18 16l-2 2 2 2"/><rect x="4" y="6" width="16" height="16" rx="2"/>',
    '<rect x="4" y="4" width="16" height="10" rx="1.5"/><path d="M2 18h20l-2-3H4Z"/>',
    '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'
  ];
  const HERO_ICONS_INNER = [
    '<path d="M7 18a4 4 0 0 1-.6-7.95A5 5 0 0 1 16 8a3.5 3.5 0 0 1 1 6.9"/><path d="M6 18h12"/>',
    '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.66 3.58 3 8 3s8-1.34 8-3V5"/><path d="M4 12c0 1.66 3.58 3 8 3s8-1.34 8-3"/>',
    '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    '<path d="M8 9l-4 3 4 3"/><path d="M16 9l4 3-4 3"/>',
    '<rect x="7" y="2" width="10" height="20" rx="2"/><circle cx="12" cy="18" r="0.6" fill="#fff" stroke="none"/>'
  ];

  const buildHeroRing = (elId, icons, radiusPercent) => {
    const el = document.getElementById(elId);
    if (!el) return;
    el.innerHTML = '';
    icons.forEach((iconPath, i) => {
      const angle = (360 / icons.length) * i - 90;
      const rad = angle * Math.PI / 180;
      const x = 50 + radiusPercent * Math.cos(rad);
      const y = 50 + radiusPercent * Math.sin(rad);
      const node = document.createElement('div');
      node.className = 'hero-node';
      node.style.left = x + '%';
      node.style.top = y + '%';
      node.innerHTML = `<div class="hero-badge"><svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round">${iconPath}</svg></div>`;
      el.appendChild(node);
    });
  };
  buildHeroRing('heroRingOuter', HERO_ICONS_OUTER, 46);
  buildHeroRing('heroRingInner', HERO_ICONS_INNER, 30);

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

  /* ---------- Contact form via WhatsApp ---------- */
  const form = document.getElementById('contactForm');
  const formNote = document.getElementById('formNote');
  const WHATSAPP_NUMBER = '5547992607105';

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const nome = form.elements['nome'].value;
      const email = form.elements['email'].value;
      const servico = form.elements['servico'].value;
      const mensagem = form.elements['mensagem'].value;

      const texto =
        `Olá! Vim pelo site da Soluções da Internet.\n\n` +
        `Nome: ${nome}\n` +
        `E-mail: ${email}\n` +
        `Serviço de interesse: ${servico}\n` +
        `Mensagem: ${mensagem}`;

      window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(texto)}`, '_blank', 'noopener');

      formNote.textContent = '✅ Abrindo o WhatsApp com sua mensagem pronta para enviar.';
      form.reset();
    });
  }
})();
