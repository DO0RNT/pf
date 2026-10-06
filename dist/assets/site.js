(() => {
  'use strict';
  const data = window.NHT_PORTFOLIO;
  if (!data) return;
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const placeholder = value => value == null || value === '' ? 'To be added' : String(value);
  const fileUrl = value => {
    const url = new URL(value, document.baseURI);
    const localPreview = new URL(document.baseURI).protocol === 'file:' && url.protocol === 'file:';
    if (!localPreview && !['http:', 'https:'].includes(url.protocol)) throw new Error('Attachment must use a local file or HTTP(S) URL.');
    return url.href;
  };

  $$('[data-name]').forEach(el => { el.textContent = data.name; });
  $$('[data-introduction]').forEach(el => { el.textContent = data.introduction; });
  $$('[data-story]').forEach(el => { el.textContent = data.story; });
  $$('[data-expertise]').forEach(list => {
    list.replaceChildren(...data.expertise.map(text => { const el = document.createElement('span'); el.textContent = text; return el; }));
  });
  $$('[data-skill-list]').forEach(list => {
    list.replaceChildren(...(data.skills[list.dataset.skillList] || []).map(text => { const el = document.createElement('li'); el.textContent = text; return el; }));
  });
  $$('[data-education]').forEach(el => { el.textContent = placeholder(data.education[el.dataset.education]); });
  if (data.portrait) {
    $$('.portrait').forEach(frame => {
      try {
        const img = document.createElement('img');
        img.src = fileUrl(data.portrait);
        img.alt = data.name;
        img.className = 'portrait-photo';
        img.addEventListener('load', () => { frame.replaceChildren(img); frame.classList.add('has-image'); }, { once: true });
      } catch { /* Keep the truthful initials placeholder for invalid files. */ }
    });
  }
  $$('[data-contact]').forEach(row => {
    const type = row.dataset.contact;
    const value = data.contact[type];
    if (!value) return;
    const node = $('.contact-value', row);
    let href;
    try {
      if (type === 'email') href = 'mailto:' + value;
      else if (type === 'phone') href = 'tel:' + value.replace(/[^+\d]/g, '');
      else href = fileUrl(value);
    } catch { return; }
    const link = document.createElement('a');
    link.href = href;
    link.className = 'contact-value';
    link.textContent = type === 'linkedin' ? 'LinkedIn profile' : type === 'github' ? 'GitHub profile' : value;
    if (['linkedin', 'github'].includes(type)) { link.target = '_blank'; link.rel = 'noopener noreferrer'; }
    node.replaceWith(link);
    const arrow = $('.arrow', row);
    if (arrow) arrow.hidden = false;
  });

  const menuButton = $('.menu-toggle');
  const menu = $('.mobile-nav');
  function closeMenu(returnFocus = false) {
    if (!menu || menu.hidden) return;
    menu.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open navigation');
    if (returnFocus) menuButton.focus();
  }
  if (menuButton && menu) {
    menuButton.hidden = false;
    menuButton.addEventListener('click', () => {
      const open = menu.hidden;
      menu.hidden = !open;
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    });
    document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(true); });
    document.addEventListener('click', event => { if (!menu.contains(event.target) && !menuButton.contains(event.target)) closeMenu(); });
    const wideScreen = window.matchMedia('(min-width: 681px)');
    wideScreen.addEventListener('change', event => { if (event.matches) closeMenu(); });
  }

  if ('IntersectionObserver' in window && !reduced.matches) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.remove('is-waiting'); observer.unobserve(entry.target); } });
    }, { threshold: .12 });
    $$('.reveal').forEach(el => {
      if (el.getBoundingClientRect().top > window.innerHeight) { el.classList.add('is-waiting'); observer.observe(el); }
    });
    reduced.addEventListener('change', event => { if (event.matches) { $$('.is-waiting').forEach(el => el.classList.remove('is-waiting')); observer.disconnect(); } });
  }

  const carousel = $('[data-carousel]');
  if (!carousel || data.projects.length !== 3) return;
  const panels = $$('.project-panel', carousel);
  const selectors = $$('.project-selector', carousel);
  const selectorGroup = $('.project-selectors', carousel);
  const toggle = $('[data-action="pause"]', carousel);
  const toggleLabel = $('[data-rotation-label]', toggle);
  const toggleIcon = $('[data-rotation-icon]', toggle);
  const note = $('.rotation-note', carousel);
  const progress = $('.rotation-track span', carousel);
  const status = $('[data-project-status]');
  const dialog = $('.preview-dialog');
  let current = 0;
  let rotationRequested = !reduced.matches;
  let hovering = false;
  let viewerOpen = false;
  let timer = null;
  let progressAnimation = null;
  let slideAnimation = null;
  let previewTrigger = null;
  const duration = 8000;

  function makeAttachment(project) {
    const file = project.attachment;
    const url = fileUrl(file.src);
    if (file.type === 'pdf') {
      const object = document.createElement('object');
      object.type = 'application/pdf';
      object.data = url;
      object.setAttribute('aria-label', file.alt || 'Project PDF attachment');
      const fallback = document.createElement('p');
      fallback.className = 'pdf-fallback';
      fallback.textContent = 'PDF preview is unavailable in this browser. ';
      const link = document.createElement('a');
      link.href = url;
      link.target = '_blank';
      link.rel = 'noopener';
      link.textContent = 'Open the PDF';
      fallback.append(link);
      object.append(fallback);
      return object;
    }
    const img = document.createElement('img');
    img.src = url;
    img.alt = file.alt || 'Project image attachment';
    img.width = 1600;
    img.height = 1100;
    img.decoding = 'async';
    return img;
  }

  panels.forEach((panel, i) => {
    const project = data.projects[i];
    panel.dataset.tone = project.tone;
    $('[data-project-title]', panel).textContent = project.title;
    $('[data-project-intro]', panel).textContent = project.introduction;
    $('[data-project-role]', panel).textContent = placeholder(project.role);
    $('[data-project-achievements]', panel).textContent = placeholder(project.achievements);
    const screen = $('.attachment-screen', panel);
    try {
      screen.replaceChildren(makeAttachment(project));
      if (project.attachment.placeholder) {
        const label = document.createElement('span');
        label.className = 'attachment-empty';
        label.textContent = 'Image placeholder';
        label.setAttribute('aria-hidden', 'true');
        screen.append(label);
      }
      $('.attachment-meta', panel).textContent = project.attachment.type === 'pdf' ? 'PDF attachment' : 'Image attachment';
      $('[data-open-preview]', panel).hidden = false;
    } catch {
      screen.textContent = 'Attachment to be added.';
    }
  });
  $$('.js-only', carousel).forEach(el => { el.hidden = false; });

  function syncRotation() {
    clearTimeout(timer);
    timer = null;
    if (progressAnimation) progressAnimation.cancel();
    progress.style.width = '0';
    toggle.disabled = reduced.matches;
    toggle.setAttribute('aria-label', reduced.matches ? 'Automatic rotation disabled for reduced motion' : rotationRequested ? 'Pause automatic project rotation' : 'Start automatic project rotation');
    toggleLabel.textContent = reduced.matches ? 'Manual' : rotationRequested ? 'Pause' : 'Play';
    toggleIcon.textContent = rotationRequested && !reduced.matches ? 'Ⅱ' : '▷';
    note.textContent = reduced.matches ? 'Reduced motion · browse projects manually' : rotationRequested ? 'Rotates every 8 seconds · pause anytime' : 'Rotation paused · browse at your own pace';
    carousel.setAttribute('data-playing', String(rotationRequested && !reduced.matches));
    if (!rotationRequested || reduced.matches || hovering || viewerOpen || document.hidden) return;
    if (typeof progress.animate === 'function') {
      progressAnimation = progress.animate([{ width: '0%' }, { width: '100%' }], { duration, easing: 'linear', fill: 'forwards' });
    }
    timer = setTimeout(() => { activate(current + 1, false); }, duration);
  }

  function activate(index, manual = true) {
    const next = (index + panels.length) % panels.length;
    const direction = next === (current + 1) % panels.length ? 1 : -1;
    if (manual) rotationRequested = false;
    if (slideAnimation) slideAnimation.cancel();
    panels.forEach((panel, i) => { panel.hidden = i !== next; });
    selectors.forEach((selector, i) => { selector.setAttribute('aria-pressed', String(i === next)); });
    selectorGroup.style.setProperty('--active', String(next));
    current = next;
    if (!reduced.matches && typeof panels[next].animate === 'function') {
      slideAnimation = panels[next].animate([{ opacity: 0, transform: `translateX(${direction * 18}px)` }, { opacity: 1, transform: 'translateX(0)' }], { duration: 470, easing: 'cubic-bezier(.22,1,.36,1)' });
    }
    if (manual) {
      status.textContent = `Project ${current + 1} of 3. ${data.projects[current].title}.`;
      const url = new URL(window.location.href);
      url.searchParams.set('project', String(current + 1));
      try { window.history.replaceState(null, '', url); } catch { /* Local file previews may restrict the History API. */ }
    }
    syncRotation();
  }

  $('[data-action="prev"]', carousel).addEventListener('click', () => { activate(current - 1); });
  $('[data-action="next"]', carousel).addEventListener('click', () => { activate(current + 1); });
  selectors.forEach((selector, i) => { selector.addEventListener('click', () => { activate(i); }); });
  toggle.addEventListener('click', () => { rotationRequested = !rotationRequested; syncRotation(); });
  carousel.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      activate(current + (event.key === 'ArrowLeft' ? -1 : 1));
    }
  });
  carousel.addEventListener('focusin', event => {
    if (event.target !== toggle && event.target.matches(':focus-visible')) { rotationRequested = false; syncRotation(); }
  });
  carousel.addEventListener('pointerenter', event => { if (event.pointerType === 'mouse') { hovering = true; syncRotation(); } });
  carousel.addEventListener('pointerleave', event => { if (event.pointerType === 'mouse') { hovering = false; syncRotation(); } });
  document.addEventListener('visibilitychange', syncRotation);
  reduced.addEventListener('change', () => { rotationRequested = false; syncRotation(); });

  if (dialog) {
    panels.forEach((panel, i) => {
      $('[data-open-preview]', panel).addEventListener('click', event => {
        const project = data.projects[i];
        previewTrigger = event.currentTarget;
        rotationRequested = false;
        viewerOpen = true;
        syncRotation();
        $('[data-preview-title]', dialog).textContent = `Project ${String(i + 1).padStart(2, '0')} · attachment`;
        $('[data-preview-content]', dialog).replaceChildren(makeAttachment(project));
        $('[data-preview-description]', dialog).textContent = project.attachment.placeholder ? 'Blank image placeholder · add your project file later.' : project.attachment.alt || 'Project attachment';
        $('[data-preview-file]', dialog).href = fileUrl(project.attachment.src);
        dialog.showModal();
      });
    });
    $('[data-close-preview]', dialog).addEventListener('click', () => { dialog.close(); });
    dialog.addEventListener('click', event => {
      if (event.target === dialog) {
        const bounds = dialog.getBoundingClientRect();
        if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
      }
    });
    dialog.addEventListener('close', () => {
      viewerOpen = false;
      $('[data-preview-content]', dialog).replaceChildren();
      if (previewTrigger) previewTrigger.focus();
      syncRotation();
    });
  }

  const initial = Number(new URL(window.location.href).searchParams.get('project'));
  if (Number.isInteger(initial) && initial >= 1 && initial <= 3) activate(initial - 1);
  else syncRotation();
})();
