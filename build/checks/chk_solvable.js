// Generate many grids in every game and mode; every one must be solvable with 9 distinct answers.
const { chromium } = require('playwright');
const files = ['hardwood-grid.html','hook-grid.html','swiftie-grid.html','zeppelin-grid.html','flannel-grid.html','wave-grid.html','ride-grid.html','wizard-grid.html','galaxy-grid.html','throne-grid.html','scranton-grid.html'];
(async () => {
  const b = await chromium.launch();
  for (const f of files) {
    const p = await b.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto('file://' + process.cwd() + '/' + f); await p.waitForTimeout(150);
    const modes = (await p.$('#mode-hard')) ? ['medium', 'hard'] : ['only'];
    const res = {};
    for (const m of modes) {
      if (m !== 'only') await p.click('#mode-' + m);
      res[m] = await p.evaluate(() => { let bad = 0, n = 0;
        for (let i = 0; i < 300; i++) { document.getElementById('random').click(); n++; if (!window.__solvable()) bad++; }
        document.getElementById('today').click(); const today = window.__solvable();
        return { grids: n, unsolvable: bad, todaySolvable: today }; });
    }
    console.log(f.padEnd(22), JSON.stringify(res), errs.length ? errs : '');
    await p.close();
  }
  await b.close();
})();
