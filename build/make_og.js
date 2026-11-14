// Renders 1200x630 link-preview images for each game page.
const { chromium } = require('playwright');
const games = [
  ['og-flannel-grid.png', 'Flannel Grid', "'90s alternative", '#131310', '#efece4', '#e8604f', '#6fc39a'],
  ['og-first-wave-grid.png', 'First Wave Grid', 'New wave & post-punk', '#110d22', '#f3efff', '#ff4fa3', '#33d6e6'],
  ['og-hook-grid.png', 'Hook Grid', '2010s pop hits', '#130e20', '#f2edfb', '#ff4f96', '#6aa0ff'],
  ['og-swiftie-grid.png', 'Swiftie Grid', 'Taylor Swift, album by album', '#0e1024', '#eef0ff', '#b49bff', '#f08fc6'],
  ['og-zeppelin-grid.png', 'Zeppelin Grid', 'Led Zeppelin deep cuts', '#141210', '#f1ebe3', '#e0654f', '#d8b25a'],
  ['og-ride-grid.png', 'Ride Grid', 'Disney parks trivia', '#0c1820', '#eef5f8', '#ff7a5c', '#5cc9e0'],
  ['og-index.png', 'Grid Games', 'Daily music trivia', '#141312', '#f1eee9', '#ef6a5c', '#6fc39a'],
];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  for (const [file, name, sub, bg, ink, a1, a2] of games) {
    const pattern = [1,0,1,0,1,1,1,0,1];
    const cells = pattern.map((on, i) => `<div style="border-radius:22px;background:${on ? (i % 2 ? a2 : a1) : 'transparent'};border:4px solid ${on ? 'transparent' : ink + '44'}"></div>`).join('');
    await p.setContent(`<body style="margin:0;width:1200px;height:630px;background:${bg};color:${ink};font-family:Helvetica,Arial,sans-serif;display:flex;align-items:center;gap:70px;padding:0 90px;box-sizing:border-box">
      <div style="display:grid;grid-template-columns:repeat(3,120px);grid-template-rows:repeat(3,120px);gap:18px;flex:none">${cells}</div>
      <div style="display:flex;flex-direction:column;gap:18px;min-width:0">
        <div style="font-size:84px;font-weight:800;line-height:1;letter-spacing:-2px">${name}</div>
        <div style="font-size:40px;opacity:.75">${sub}</div>
        <div style="font-size:34px;color:${a1};font-weight:700;margin-top:10px">Play today’s grid →</div>
      </div></body>`);
    await p.screenshot({ path: 'site/' + file });
  }
  await b.close(); console.log('made', games.length);
})();
