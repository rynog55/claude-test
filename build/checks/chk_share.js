// Tests the Share score / Copy score feature on the site pages (simulated stats database).
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const f of ['flannel-grid.html', 'swiftie-grid.html']) {
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, permissions: ['clipboard-read', 'clipboard-write'] });
    const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.route('**/rest/v1/rpc/**', r => r.request().url().endsWith('grid_stats')
      ? r.fulfill({ status: 200, contentType: 'application/json', body: '{"players":2,"answers":[]}' })
      : r.fulfill({ status: 204, body: '' }));
    await p.goto('file://' + process.cwd() + '/site/' + f); await p.waitForTimeout(300);
    const ok = await p.evaluate(() => window.__gridTest.firstAnswer());
    await p.click('#cell-0'); await p.fill('#q', ok.slice(0, 12)); await p.waitForTimeout(100);
    for (const bt of await p.$$('#results button')) { if ((await bt.textContent()).startsWith(ok)) { await bt.click(); break; } }
    await p.waitForTimeout(300); await p.click('#giveup'); await p.waitForTimeout(300);
    const text = await p.evaluate(() => window.__gridTest.shareText());
    await p.click('#copyScore'); await p.waitForTimeout(300);
    const btn = await p.textContent('#copyScore');
    const clip = await p.evaluate(() => navigator.clipboard.readText());
    const og = await p.$eval('meta[property="og:image"]', m => m.content); const html = await p.evaluate(async () => { const it = await navigator.clipboard.read(); const t = it[0].types.includes('text/html') ? await (await it[0].getType('text/html')).text() : ''; return t; }); const home = await p.$eval('.topnav a', a => a.getAttribute('href'));
    if (f === 'flannel-grid.html') await p.screenshot({ path: 'share.png' });
    console.log(f, JSON.stringify({ errs, text, btn, clip, html, home }));
    await ctx.close();
  }
  await b.close();
})();
