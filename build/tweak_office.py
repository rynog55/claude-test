"""Scranton Grid: allow single-answer squares (small cast) and style the title like a boxed, lowercase typewriter title card."""
t = open('scranton-grid.html').read()
for a, b in [("const MIN = MODE === 'medium' ? 2 : 1;", "const MIN = 1;"),
             ("if (ok && thin <= 2) return", "if (ok && thin <= (MODE === 'medium' ? 3 : 5)) return"),
             ("h1 span { color: var(--accent); }", "h1 { text-transform: lowercase; font-weight: 700; display: inline-block; border: 3px solid var(--ink); padding: 4px 14px 8px; letter-spacing: -.02em; font-size: clamp(22px, 7vw, 40px); }\nh1 span { color: var(--accent-2); }\n.rowhead { font-size: clamp(12px, 3.4vw, 16px) !important; letter-spacing: -.03em !important; }")]:
    assert a in t, a; t = t.replace(a, b)
open('scranton-grid.html', 'w').write(t); print('tweaked')
