const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('file://'+process.cwd()+'/site/flannel-grid.html');await p.waitForTimeout(4000);
console.log(JSON.stringify({errs,statline:await p.textContent('#statline')}));await b.close();})();
