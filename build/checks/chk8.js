const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.cwd()+'/hook-grid.html');
const rows=await p.evaluate(()=>{const rows={};for(let i=0;i<300;i++){document.getElementById('random').click();
  document.querySelectorAll('.rowhead').forEach(h=>rows[h.firstChild.textContent]=(rows[h.firstChild.textContent]||0)+1);}return rows;});
console.log(JSON.stringify({errs,n:Object.keys(rows).length,sample:Object.keys(rows).filter(k=>k.includes(' ')).slice(0,15)}));await b.close();})();
