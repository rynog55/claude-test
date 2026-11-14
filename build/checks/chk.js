const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.cwd()+'/hardwood-grid.html');
await p.click('#cell-0');await p.fill('#q','du');await p.waitForTimeout(100);
const r=await p.$$eval('#results button',x=>x.length);await p.click('#close');
for(let i=0;i<30;i++) await p.click('#random');
const w=await p.evaluate(()=>document.documentElement.scrollWidth);
await p.screenshot({path:'hg.png'});console.log({errs,r,w});await b.close();})();
