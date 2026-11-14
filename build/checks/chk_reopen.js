// Finish a grid, reload the page, and confirm the share buttons and tap hint show on the finished grid.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
  const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await ctx.route('**/rest/v1/rpc/**', r => r.request().url().endsWith('grid_stats')
    ? r.fulfill({ status: 200, contentType: 'application/json', body: '{"players":1,"answers":[]}' })
    : r.fulfill({ status: 204, body: '' }));
  const url = 'file://' + process.cwd() + '/site/flannel-grid.html';
  await p.goto(url); await p.waitForTimeout(300);
  await p.click('#giveup'); await p.waitForTimeout(300);
  await p.reload(); await p.waitForTimeout(800);
  const share = await p.$('#shareScore') !== null;
  const hint = (await p.textContent('#sumText')).includes('Tap any square');
  console.log(JSON.stringify({ errs, shareButtonAfterReload: share, hintAfterReload: hint }));
  await b.close();
})();
