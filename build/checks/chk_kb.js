const {chromium}=require('playwright');
const files=['hardwood-grid.html','hook-grid.html','swiftie-grid.html','zeppelin-grid.html','flannel-grid.html','wave-grid.html'];
(async()=>{const b=await chromium.launch();
for(const f of files){const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
  await p.goto('file://'+process.cwd()+'/'+f);
  await p.click('#cell-0'); await p.setViewportSize({width:390,height:420}); // simulate keyboard taking half the screen
  await p.fill('#q','the'); await p.waitForTimeout(150);
  const r=await p.evaluate(()=>{const s=document.getElementById('sheet').getBoundingClientRect();const q=document.getElementById('q').getBoundingClientRect();
    const first=document.querySelector('#results button');const fr=first?first.getBoundingClientRect():null;
    return {sheetBottom:Math.round(s.bottom),inputBottom:Math.round(q.bottom),firstResultBottom:fr?Math.round(fr.bottom):null,vh:innerHeight};});
  if(f==='hook-grid.html') await p.screenshot({path:'kb.png'});
  console.log(f, JSON.stringify(r), errs.length?errs:''); await p.close();}
await b.close();})();
