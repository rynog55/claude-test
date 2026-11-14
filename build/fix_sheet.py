import re, sys
NEW_CSS = """.sheet {
  position: fixed; left: 0; right: 0; top: var(--vv-top, 0px); z-index: 6; background: var(--panel); color: var(--ink);
  border-radius: 0 0 18px 18px; box-shadow: 0 8px 30px rgba(0,0,0,.25);
  padding-top: calc(12px + env(safe-area-inset-top, 0px)); padding-bottom: 12px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px));
  max-height: var(--vv-h, 85%); display: flex; flex-direction: column;
}"""
NEW_JS = """function fitSheet() {
  const sh = document.getElementById('sheet'), vv = window.visualViewport;
  if (!sh) return;
  const h = vv ? vv.height : innerHeight, top = vv ? vv.offsetTop : 0;
  sh.style.setProperty('--vv-h', Math.round(h * 0.94) + 'px');
  sh.style.setProperty('--vv-top', Math.round(top) + 'px');
}
if (window.visualViewport) { visualViewport.addEventListener('resize', fitSheet); visualViewport.addEventListener('scroll', fitSheet); }
addEventListener('resize', fitSheet); fitSheet();
$('q').addEventListener('focus', () => setTimeout(fitSheet, 300));
"""
for f in sys.argv[1:]:
    t = open(f).read()
    if 'function fitSheet()' in t: print('already', f); continue
    t, n = re.subn(r'\.sheet \{\n.*?\n\}', NEW_CSS, t, count=1, flags=re.S)
    assert n == 1, ('css', f)
    anchor = "$('q').addEventListener('input', renderResults);"
    assert anchor in t, ('js', f)
    t = t.replace(anchor, NEW_JS + anchor, 1)
    open(f, 'w').write(t); print('patched', f)
