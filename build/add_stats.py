"""Turn an artifact grid page into a standalone site page with shared daily stats (Supabase)."""
import re, sys, json
SB_URL = 'https://bfohdusslfiilrmhrnlp.supabase.co'
CSS = """
.statline { margin: 2px 0 0; color: var(--muted); font-size: 12.5px; font-variant-numeric: tabular-nums; }
.statline b { color: var(--ink); }
.cell.over-tap { cursor: pointer; }
.cell.over-tap:hover { border-color: var(--accent); }
.cell .top { font-size: 10px; color: var(--muted); text-align: center; line-height: 1.25; }
.cell .top b { color: var(--ink); font-weight: 700; }
.ans { list-style: none; border-bottom: 1px solid var(--line); padding: 10px 4px; display: flex; flex-direction: column; gap: 4px; }
.ans-top { display: flex; justify-content: space-between; gap: 10px; align-items: baseline; }
.ans-top .t { font: 600 15px var(--font-body); min-width: 0; overflow-wrap: anywhere; }
.ans-top .p { font: 700 14px var(--font-body); font-variant-numeric: tabular-nums; color: var(--accent); flex: none; }
.ans small { color: var(--muted); font-size: 12px; }
.ans .bar { height: 5px; border-radius: 3px; background: var(--line); overflow: hidden; }
.ans .bar i { display: block; height: 100%; background: var(--accent); }
.ans.mine { background: var(--hit-soft); border-radius: 8px; }
.topnav { margin: 0 0 -6px; }
.topnav a { display: inline-flex; align-items: center; gap: 6px; font: 600 13px var(--font-body); color: var(--muted); text-decoration: none; padding: 6px 12px 6px 8px; border: 1px solid var(--line); border-radius: 999px; background: var(--panel); }
.topnav a:hover, .topnav a:focus-visible { color: var(--ink); border-color: var(--accent); outline: none; }
.topnav svg { width: 16px; height: 16px; flex: none; }
.share-row { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; margin-top: 6px; }
.ans .mine-tag { font-size: 11px; font-weight: 700; color: var(--hit); text-transform: uppercase; letter-spacing: .06em; }
"""
JS = r"""
const SB_URL = '__SB_URL__', SB_KEY = '__SB_KEY__', GAME = '__GAME__';
let PLAYER = null;
try { PLAYER = localStorage.getItem('gg:player'); if (!PLAYER) { PLAYER = crypto.randomUUID(); localStorage.setItem('gg:player', PLAYER); } } catch (e) { PLAYER = (crypto.randomUUID ? crypto.randomUUID() : null); }
let STATS = null, STATS_STATE = 'idle';
const gridKey = () => ((typeof MODE !== 'undefined') ? MODE : 'std') + ':' + seed;
const isDaily = () => typeof seed === 'string' && seed.startsWith('daily-');
const songKey = s => s.title + ' | ' + (s.credit || s.album || '');
async function rpc(fn, body) {
  const r = await fetch(SB_URL + '/rest/v1/rpc/' + fn, { method: 'POST', headers: { apikey: SB_KEY, Authorization: 'Bearer ' + SB_KEY, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  if (!r.ok) throw new Error('HTTP ' + r.status);
  const t = await r.text(); return t ? JSON.parse(t) : null;
}
async function loadStats() {
  if (!isDaily() || !PLAYER) { STATS = null; STATS_STATE = 'off'; render(); return; }
  const k = gridKey(); STATS_STATE = STATS ? STATS_STATE : 'loading'; renderStats();
  try { const s = await rpc('grid_stats', { p_game: GAME, p_grid: k }); if (k === gridKey()) { STATS = s; STATS_STATE = 'ok'; render(); } }
  catch (e) { if (k === gridKey()) { STATS_STATE = 'error'; renderStats(); } }
}
function record(cell, answer) {
  if (!isDaily() || !PLAYER) return Promise.resolve();
  return rpc('record_answer', { p_game: GAME, p_grid: gridKey(), p_player: PLAYER, p_cell: cell, p_answer: answer }).catch(() => {});
}
function pickCount(cell, s) { if (!STATS) return 0; const a = STATS.answers.find(x => x.cell === cell && x.answer === songKey(s)); return a ? a.n : 0; }
function pct(n) { return STATS && STATS.players ? Math.round(100 * n / STATS.players) : 0; }
function renderStats() {
  const el = $('statline'); if (!el) return;
  if (!isDaily()) { el.textContent = 'Player stats are kept for the daily grid only.'; return; }
  if (STATS_STATE === 'loading') { el.textContent = 'Loading today’s players…'; return; }
  if (STATS_STATE === 'error') { el.textContent = 'Player stats aren’t reachable right now.'; return; }
  if (!STATS) { el.textContent = ''; return; }
  const n = STATS.players; el.innerHTML = '';
  const b = document.createElement('b'); b.textContent = n; el.append(b, n === 1 ? ' player today' : ' players today');
}
function decorate() {
  const over = done();
  for (let idx = 0; idx < 9; idx++) {
    const btn = $('cell-' + idx); if (!btn) continue;
    const val = S.cells[idx];
    if (val !== null && STATS && STATS.players) {
      const r = btn.querySelector('.rare'); if (r) r.textContent = pct(pickCount(idx, SONGS[val])) + '% picked this';
    }
    if (!over) continue;
    btn.disabled = false; btn.classList.add('over-tap');
    btn.onclick = () => openAnswers(idx);
    if (val === null && STATS && STATS.answers.some(a => a.cell === idx)) {
      const best = STATS.answers.filter(a => a.cell === idx).sort((a, b) => b.n - a.n)[0];
      const name = btn.querySelector('.name'); if (name) name.remove();
      const top = document.createElement('span'); top.className = 'top';
      top.append('Most picked', document.createElement('br'));
      const bb = document.createElement('b'); bb.textContent = best.answer.split(' | ')[0]; top.append(bb, ' · ' + pct(best.n) + '%');
      btn.appendChild(top);
    }
  }
  if (over) addShareRow();
  if (over) { const p = $('sumText'); const hint = ' Tap any square to see every answer that worked and how often players picked it.'; if (p && !p.textContent.includes(hint.trim())) p.textContent += hint; }
}
function openAnswers(idx) {
  active = null;
  const row = G.rows[Math.floor(idx / 3)], c = G.cols[idx % 3];
  $('prompt').textContent = rowLabel(row)[0] + ' + ' + COLS[c][0];
  $('q').hidden = true;
  const ul = $('results'); ul.innerHTML = '';
  const list = answers(row, c).map(s => ({ s, n: pickCount(idx, s) })).sort((a, b) => b.n - a.n || a.s.title.localeCompare(b.s.title));
  const hint = document.createElement('li'); hint.className = 'hint';
  hint.textContent = list.length + (list.length === 1 ? ' answer worked' : ' answers worked') + (isDaily() && STATS ? ' · ' + STATS.players + (STATS.players === 1 ? ' player today' : ' players today') : '');
  ul.appendChild(hint);
  for (const { s, n } of list) {
    const li = document.createElement('li'); li.className = 'ans' + (S.cells[idx] === s.i ? ' mine' : '');
    const top = document.createElement('div'); top.className = 'ans-top';
    const t = document.createElement('span'); t.className = 't'; t.textContent = s.title;
    const p = document.createElement('span'); p.className = 'p'; p.textContent = isDaily() && STATS ? pct(n) + '%' : '';
    top.append(t, p); li.appendChild(top);
    const sm = document.createElement('small'); sm.textContent = s.credit || s.album || ''; li.appendChild(sm);
    if (isDaily() && STATS) { const bar = document.createElement('div'); bar.className = 'bar'; const i = document.createElement('i'); i.style.width = pct(n) + '%'; bar.appendChild(i); li.appendChild(bar); }
    if (S.cells[idx] === s.i) { const m = document.createElement('span'); m.className = 'mine-tag'; m.textContent = 'Your pick'; li.appendChild(m); }
    ul.appendChild(li);
  }
  $('scrim').hidden = false; $('sheet').hidden = false;
  if (typeof fitSheet === 'function') fitSheet();
}
window.__gridTest = { firstAnswer: () => answers(G.rows[0], G.cols[0])[0].title };

const LAUNCH = Date.UTC(2026, 10, 14);
function puzzleNo() { if (!isDaily()) return null; const d = seed.slice(6).split('-').map(Number); return Math.round((Date.UTC(d[0], d[1] - 1, d[2]) - LAUNCH) / 864e5) + 1; }
function shareText() {
  const n = S.cells.filter(c => c !== null).length, no = puzzleNo();
  const mode = (typeof MODE !== 'undefined') ? ' (' + MODE[0].toUpperCase() + MODE.slice(1) + ')' : '';
  const head = document.title + (no ? ' #' + no : ' · random grid') + mode + ' ' + n + '/9';
  const rows = [0, 1, 2].map(r => [0, 1, 2].map(c => S.cells[r * 3 + c] !== null ? '\u{1F7E9}' : '\u{1F7E5}').join('')).join('\n');
  return head + '\n' + rows;
}
const shareUrl = () => location.origin + location.pathname;
async function shareScore(btn) {
  const text = shareText(), url = shareUrl();
  if (navigator.share) {
    try { await navigator.share({ text, url }); return; }
    catch (e) { if (e && e.name === 'AbortError') return; }
  }
  copyScore($('copyScore'));
}
async function copyScore(btn) {
  const text = shareText(), url = shareUrl(), plain = text + '\n' + url;
  const name = document.title, esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const html = '<a href="' + url + '">' + esc(name) + '</a>' + esc(text.slice(name.length)).split('\n').join('<br>');
  let ok = false;
  try {
    if (window.ClipboardItem && navigator.clipboard && navigator.clipboard.write) {
      await navigator.clipboard.write([new ClipboardItem({ 'text/plain': new Blob([plain], { type: 'text/plain' }), 'text/html': new Blob([html], { type: 'text/html' }) })]);
      ok = true;
    }
  } catch (e) {}
  if (!ok) { try { await navigator.clipboard.writeText(plain); ok = true; } catch (e) {} }
  if (btn) { btn.textContent = ok ? 'Copied!' : 'Couldn’t copy'; setTimeout(() => { btn.textContent = 'Copy score'; }, 2000); }
}
function addShareRow() {
  const sum = $('summary'); if (!sum || $('shareRow')) return;
  const row = document.createElement('div'); row.className = 'share-row'; row.id = 'shareRow';
  const a = document.createElement('button'); a.type = 'button'; a.className = 'btn primary'; a.id = 'shareScore'; a.textContent = 'Share score';
  const b = document.createElement('button'); b.type = 'button'; b.className = 'btn'; b.id = 'copyScore'; b.textContent = 'Copy score';
  a.addEventListener('click', () => shareScore(a)); b.addEventListener('click', () => copyScore(b));
  row.append(a, b); sum.appendChild(row);
}
window.__gridTest.shareText = () => shareText();
const _render = render; render = function () { _render(); renderStats(); decorate(); };
const _openSheet = openSheet; openSheet = function (idx) { $('q').hidden = false; _openSheet(idx); };
const _load = load; load = function (sd) { STATS = null; STATS_STATE = 'idle'; _load(sd); loadStats(); };
const _guess = guess; guess = function (s) {
  const idx = active; if (idx === null) return;
  const before = S.cells[idx]; _guess(s);
  const ok = before === null && S.cells[idx] === s.i;
  record(ok ? idx : 0, ok ? songKey(s) : '').then(loadStats);
};
"""
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#111111">
{title}
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{name}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://rynog55.github.io/claude-test/site/{img}">
<meta property="og:url" content="https://rynog55.github.io/claude-test/site/{page}">
<meta name="twitter:card" content="summary_large_image">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;font:14px system-ui,-apple-system,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
"""
def build(src, dst, game, key):
    t = open(src).read()
    m = re.search(r'<title>.*?</title>\n?', t); title = m.group(0).strip(); t = t.replace(m.group(0), '', 1)
    t = t.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
    t = t.replace('</style>', CSS + '</style>', 1)
    h = '  <header>'; assert h in t
    t = t.replace(h, '  <nav class="topnav" aria-label="Site"><a href="./"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>All games</a></nav>\n' + h, 1)
    a = '<p class="sub" id="label">Daily grid</p>'; assert a in t
    t = t.replace(a, a + '\n      <p class="statline" id="statline" aria-live="polite"></p>', 1)
    anchor = "$('q').addEventListener('input', renderResults);"; assert anchor in t
    js = JS.replace('__SB_URL__', SB_URL).replace('__SB_KEY__', key).replace('__GAME__', game)
    t = t.replace(anchor, js + anchor, 1)
    for fn in ('function render(', 'function openSheet(', 'function load(', 'function guess(', 'const done', 'const answers', 'const rowLabel'):
        assert fn in t, (src, fn)
    name = re.sub(r'</?title>', '', title)
    desc = 'Today’s 3×3 music trivia grid. Can you fill every square?'
    page = dst.split('/')[-1]; img = 'og-' + page.replace('.html', '.png')
    open(dst, 'w').write(HEAD.format(title=title, name=name, desc=desc, img=img, page=page) + t + '\n</body>\n</html>\n')
if __name__ == '__main__':
    key = sys.argv[1]
    for src, dst, game in [('hook-grid.html', 'site/hook-grid.html', 'hook'), ('swiftie-grid.html', 'site/swiftie-grid.html', 'swiftie'),
                           ('zeppelin-grid.html', 'site/zeppelin-grid.html', 'zeppelin'), ('flannel-grid.html', 'site/flannel-grid.html', 'flannel'),
                           ('wave-grid.html', 'site/first-wave-grid.html', 'firstwave')]:
        build(src, dst, game, key); print('built', dst)
