"""Only accept grids that can be filled with 9 different answers (each answer is usable once).
Covers the rule "no two squares whose only answer is the same", plus larger versions of the same trap."""
import re, sys
FN = """function solvable(rs, cs) {
  // Bipartite matching: can every square get its own distinct answer?
  const lists = [];
  for (const r of rs) for (const c of cs) lists.push(answers(r, c).map(x => x.i));
  const owner = new Map();
  const tryCell = (k, seen) => {
    for (const a of lists[k]) {
      if (seen.has(a)) continue; seen.add(a);
      if (!owner.has(a) || tryCell(owner.get(a), seen)) { owner.set(a, k); return true; }
    }
    return false;
  };
  for (let k = 0; k < lists.length; k++) if (!tryCell(k, new Set())) return false;
  return true;
}
"""
for f in sys.argv[1:]:
    t = open(f).read()
    if 'function solvable(' in t: print('already', f); continue
    assert 'function makeGrid(' in t, f
    t = t.replace('function makeGrid(', FN + "window.__solvable = () => (G.schools ? solvable(G.schools, G.cats) : solvable(G.rows, G.cols));\n" + 'function makeGrid(', 1)
    hardwood = 'return { schools, cats }' in t
    args = 'schools, cats' if hardwood else 'rows, cols'
    t, n = re.subn(r'if \(ok && thin <= ', 'if (ok && solvable(' + args + ') && thin <= ', t, count=1)
    assert n == 1, f
    open(f, 'w').write(t); print('patched', f)
