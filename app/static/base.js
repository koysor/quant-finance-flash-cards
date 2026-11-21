/*
 * Shared behaviour for every page: search overlay, theme and wide mode,
 * mobile menu, random card, keyboard shortcuts.  A plain (not module, not
 * deferred) script loaded at the end of <body>, so its top-level names
 * (ALL_CARDS, CARDS_READY, goRandom, setTheme, ...) are globals for each
 * page's own scripts.  Header buttons carry data-action attributes instead
 * of inline onclick handlers, so a click before this file has loaded does
 * nothing rather than throwing a ReferenceError.
 */

/*
 * Server URLs come from FC_URLS, set in base.html just before this file
 * loads.  Caddy serves /static/* as immutable for a year and ignores ?v=, so
 * a page cached from an older deploy can run a newer copy of this file.
 * Read every URL through fcUrl() with a fallback path relative to the site
 * root (worked out from this script's own URL), so a key the page does not
 * define still resolves.
 */
const SITE_ROOT = new URL('..', document.currentScript.src).pathname;
function fcUrl(key, fallbackPath) {
  const urls = typeof FC_URLS === 'object' && FC_URLS ? FC_URLS : {};
  return urls[key] || SITE_ROOT + fallbackPath;
}

let ALL_CARDS = [];
/* Resolves once the card index has loaded; pages wait on it, never refetch. */
const CARDS_READY = fetch(fcUrl('searchData', 'search-data.json'))
  .then(r => r.json())
  .then(data => { ALL_CARDS = data; return data; });

/* ── Theme toggle ── */
function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
  if (theme !== 'barbie') document.cookie = 'theme=; max-age=0; path=/';
  updatePills(theme);
  if (typeof onThemeChange === 'function') onThemeChange(theme);
}

function updatePills(theme) {
  ['', '-m'].forEach(suffix => {
    const d = document.getElementById('btn-dark'  + suffix);
    const l = document.getElementById('btn-light' + suffix);
    const p = document.getElementById('toggle-pill' + suffix);
    if (!d || !l || !p) return;
    const active = theme === 'dark' ? d : l;
    d.classList.toggle('active', theme === 'dark');
    l.classList.toggle('active', theme === 'light');
    requestAnimationFrame(() => {
      const parentLeft = p.parentElement.getBoundingClientRect().left;
      const btnLeft    = active.getBoundingClientRect().left;
      p.style.width     = active.offsetWidth + 'px';
      p.style.transform = `translateX(${btnLeft - parentLeft - 3}px)`;
    });
  });
}

(function() {
  const t = document.documentElement.getAttribute('data-theme') || 'dark';
  requestAnimationFrame(() => updatePills(t));
})();
window.addEventListener('resize', () => {
  updatePills(document.documentElement.getAttribute('data-theme') || 'dark');
});

/* ── Font size ── */
const FONT_MIN = -2, FONT_MAX = 3;
let fontStep = parseInt(localStorage.getItem('font_size_step'), 10) || 0;

function changeFontSize(dir) {
  if (dir === 0) {
    fontStep = 0;
  } else {
    fontStep = Math.max(FONT_MIN, Math.min(FONT_MAX, fontStep + dir));
  }
  document.documentElement.style.fontSize = fontStep === 0 ? '' : (100 + fontStep * 10) + '%';
  localStorage.setItem('font_size_step', fontStep);
}

/* ── Wide mode ── */
let wideMode = localStorage.getItem('wide_mode') === 'true';

function applyWideMode(on) {
  document.documentElement.setAttribute('data-wide', on ? 'true' : 'false');
  document.getElementById('wide-icon-expand').style.display   = on ? 'none' : '';
  document.getElementById('wide-icon-contract').style.display = on ? ''     : 'none';
  document.getElementById('wide-btn').classList.toggle('active', on);
}

function toggleWideMode() {
  wideMode = !wideMode;
  localStorage.setItem('wide_mode', wideMode);
  applyWideMode(wideMode);
}

// Sync icon state on load (wide mode may have been set before paint)
applyWideMode(wideMode);

/* ── Scroll progress + back to top ── */
const scrollBar = document.getElementById('scroll-progress');
const btt       = document.getElementById('back-to-top');
window.addEventListener('scroll', () => {
  const pct = window.scrollY / Math.max(1, document.body.scrollHeight - window.innerHeight) * 100;
  scrollBar.style.width = Math.min(pct, 100) + '%';
  btt.classList.toggle('visible', window.scrollY > 400);
}, { passive: true });

/* ── Mobile menu ── */
function toggleMobileMenu() {
  const menu = document.getElementById('mobile-menu');
  const btn  = document.getElementById('nav-hamburger');
  const open = menu.classList.toggle('open');
  btn.setAttribute('aria-expanded', open);
  menu.setAttribute('aria-hidden', !open);
  if (open) updatePills(document.documentElement.getAttribute('data-theme') || 'dark');
}
function closeMenu() {
  document.getElementById('mobile-menu').classList.remove('open');
  document.getElementById('nav-hamburger').setAttribute('aria-expanded', false);
}
document.addEventListener('click', e => {
  const menu = document.getElementById('mobile-menu');
  if (menu.classList.contains('open') &&
      !menu.contains(e.target) &&
      !document.getElementById('nav-hamburger').contains(e.target)) {
    closeMenu();
  }
});

/* ── Random card ── */
function goRandom() {
  if (!ALL_CARDS.length) return;
  const visited = new Set(JSON.parse(localStorage.getItem('visited_cards') || '[]'));
  const unvisited = ALL_CARDS.filter(c => !visited.has(c.id));
  const pool = unvisited.length > 0 ? unvisited : ALL_CARDS;
  const card = pool[Math.floor(Math.random() * pool.length)];
  window.location.href = card.url;
}

/* ── Search overlay ── */
let searchFocusIdx = -1;

function openSearch() {
  document.getElementById('search-overlay').hidden = false;
  const inp = document.getElementById('search-input');
  inp.value = '';
  inp.focus();
  renderSearchResults('');
  searchFocusIdx = -1;
}
function closeSearch() { document.getElementById('search-overlay').hidden = true; }

function escHtml(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function fuzzyScore(text, query) {
  const t = text.toLowerCase(), q = query.toLowerCase();
  let score = 0, qi = 0, lastMatch = -1;
  for (let ti = 0; ti < t.length && qi < q.length; ti++) {
    if (t[ti] === q[qi]) {
      score += (ti === lastMatch + 1) ? 3 : 1;
      lastMatch = ti;
      qi++;
    }
  }
  return qi === q.length ? score : 0;
}

function renderSearchResults(query) {
  const container = document.getElementById('search-results');
  const q = query.trim();

  let matches;
  if (!q) {
    matches = ALL_CARDS.slice(0, 8);
  } else {
    matches = ALL_CARDS
      .map(c => ({
        card: c,
        score: fuzzyScore(c.name, q) * 3 +
               fuzzyScore(c.topic, q)      +
               fuzzyScore(c.tags, q)       +
               (c.blurb && c.blurb.toLowerCase().includes(q.toLowerCase()) ? 4 : 0),
      }))
      .filter(x => x.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 15)
      .map(x => x.card);
  }

  if (!matches.length) {
    container.innerHTML = `<div class="search-empty">No cards match "<em>${escHtml(q)}</em>"</div>`;
    return;
  }
  container.innerHTML = matches.map((c, i) => `
    <a class="search-result" href="${c.url}" data-idx="${i}">
      <span class="search-result-dot" style="background:${c.colour}"></span>
      <span class="search-result-info">
        <span class="search-result-name">${hl(c.name, q)}</span>
        <span class="search-result-topic">${escHtml(c.topic)}</span>
        ${q && c.blurb ? `<span class="search-result-topic">${escHtml(c.blurb.slice(0, 90))}…</span>` : ''}
      </span>
    </a>
  `).join('');
  searchFocusIdx = -1;
}

function hl(text, q) {
  const safe = escHtml(text);
  if (!q) return safe;
  const escaped = escHtml(q).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return safe.replace(
    new RegExp(`(${escaped})`, 'gi'),
    '<mark style="background:var(--accent-soft);color:var(--accent);border-radius:2px">$1</mark>'
  );
}

function moveSearchFocus(dir) {
  const results = document.querySelectorAll('.search-result');
  if (!results.length) return;
  results[Math.max(searchFocusIdx, 0)]?.classList.remove('focused');
  searchFocusIdx = Math.max(0, Math.min(searchFocusIdx + dir, results.length - 1));
  results[searchFocusIdx].classList.add('focused');
  results[searchFocusIdx].scrollIntoView({ block: 'nearest' });
}

document.getElementById('search-input').addEventListener('input', e => renderSearchResults(e.target.value));
document.getElementById('search-overlay').addEventListener('click', e => {
  if (e.target === document.getElementById('search-overlay')) closeSearch();
});

/* ── Shortcuts modal ── */
function openShortcuts()  { document.getElementById('shortcuts-overlay').hidden = false; }
function closeShortcuts() { document.getElementById('shortcuts-overlay').hidden = true; }
document.getElementById('shortcuts-overlay').addEventListener('click', e => {
  if (e.target === document.getElementById('shortcuts-overlay')) closeShortcuts();
});

/* ── Global keyboard handler ── */
document.addEventListener('keydown', e => {
  const tag = document.activeElement?.tagName;
  const inInput    = tag === 'INPUT' || tag === 'SELECT' || tag === 'TEXTAREA';
  const searchOpen = !document.getElementById('search-overlay').hidden;
  const shortcutsOpen = !document.getElementById('shortcuts-overlay').hidden;

  if (e.key === 'Escape') {
    if (searchOpen)    { closeSearch();    return; }
    if (shortcutsOpen) { closeShortcuts(); return; }
    closeMenu();
    return;
  }
  if (searchOpen) {
    if (e.key === 'ArrowDown') { e.preventDefault(); moveSearchFocus(1);  return; }
    if (e.key === 'ArrowUp')   { e.preventDefault(); moveSearchFocus(-1); return; }
    if (e.key === 'Enter') {
      const f = document.querySelector('.search-result.focused') ||
                document.querySelector('.search-result');
      if (f) { f.click(); closeSearch(); }
      return;
    }
    return;
  }
  if (inInput) return;
  if (e.key === '/')  { e.preventDefault(); openSearch();   return; }
  if (e.key === '?')  { openShortcuts();                    return; }
  if (e.key === 'r')  { goRandom();                         return; }
  if (e.key === 'g')  { window.location.href = fcUrl('graph', 'graph'); return; }
  if (e.key === 'f')  { window.location.href = fcUrl('formulas', 'formulas'); return; }
  if (e.key === 'c')  { window.location.href = fcUrl('index', ''); return; }
  if (e.key === 'w')  { toggleWideMode();                   return; }
  if (typeof handleCardNav === 'function') handleCardNav(e.key);
});

/* ── Header buttons ── */
const ACTIONS = {
  random:    goRandom,
  search:    openSearch,
  shortcuts: openShortcuts,
  wide:      toggleWideMode,
  menu:      toggleMobileMenu,
  font:      arg => changeFontSize(Number(arg)),
  theme:     arg => setTheme(arg),
};
document.addEventListener('click', e => {
  const el = e.target.closest('[data-action]');
  if (!el || !ACTIONS[el.dataset.action]) return;
  if (el.hasAttribute('data-close-menu')) closeMenu();
  ACTIONS[el.dataset.action](el.dataset.arg);
});
