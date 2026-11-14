// Tests the standalone site pages against a simulated stats database (no network).
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const files = ['scranton-grid.html'];
  for (const f of files) {
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
    const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    const db = { players: new Set(), answers: {} }; const calls = [];
    await p.route('**/rest/v1/rpc/**', async r => {
      const fn = r.request().url().split('/').pop(); const body = JSON.parse(r.request().postData() || '{}'); calls.push(fn);
      if (fn === 'record_answer') {
        db.players.add(body.p_player);
        if (body.p_answer) { const k = body.p_cell + '|' + body.p_answer; db.answers[k] = (db.answers[k] || 0) + 1; }
        return r.fulfill({ status: 204, body: '' });
      }
      const ans = Object.entries(db.answers).map(([k, n]) => ({ cell: +k.split('|')[0], answer: k.slice(k.indexOf('|') + 1), n }));
      // pretend 3 other people already played today
      return r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ players: db.players.size + 3, answers: ans }) });
    });
    await p.goto('file://' + process.cwd() + '/site/' + f); await p.waitForTimeout(300);
    const before = await p.textContent('#statline');
    const ok = await p.evaluate(() => window.__gridTest.firstAnswer()); await p.click('#cell-0');
    await p.fill('#q', ok.slice(0, 12)); await p.waitForTimeout(100);
    let clicked = false;
    for (const bt of await p.$$('#results button')) { if ((await bt.textContent()).startsWith(ok)) { await bt.click(); clicked = true; break; } }
    await p.waitForTimeout(400);
    const cell0 = await p.textContent('#cell-0'); const after = await p.textContent('#statline');
    await p.click('#giveup'); await p.waitForTimeout(400);
    await p.click('#cell-4'); await p.waitForTimeout(200);
    const sheet = await p.$$eval('#results li', x => x.slice(0, 3).map(e => e.textContent.replace(/\s+/g, ' ').trim()));
    const qHidden = await p.$eval('#q', e => e.hidden);
    if (f === 'flannel-grid.html') {
      await p.click('#close'); await p.click('#cell-0'); await p.waitForTimeout(200);
      await p.screenshot({ path: 'stats-sheet.png' });
      await p.click('#close'); await p.screenshot({ path: 'stats-grid.png' });
    }
    console.log(f, JSON.stringify({ errs, before, after, clicked, cell0, calls: [...new Set(calls)], sheet, qHidden }));
    await ctx.close();
  }
  await b.close();
})();
