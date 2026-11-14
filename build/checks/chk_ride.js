const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.cwd()+'/ride-grid.html');
const run=async()=>p.evaluate(()=>{const cats={},rows={};let minAns=99;
  for(let i=0;i<200;i++){document.getElementById('random').click();
    document.querySelectorAll('.head').forEach(h=>cats[h.firstChild.textContent]=(cats[h.firstChild.textContent]||0)+1);
    document.querySelectorAll('.rowhead').forEach(h=>rows[h.firstChild.textContent]=(rows[h.firstChild.textContent]||0)+1);}
  return {mode:document.querySelector('.mode[aria-pressed=true]').textContent,cats,rows};});
const med=await run(); await p.click('#mode-hard'); const hard=await run();
await p.click('#mode-medium'); await p.click('#today');
// give up to reveal answers and count shown answers per square
await p.click('#giveup'); const reveal=await p.$$eval('.cell.reveal .name',x=>x.map(e=>e.textContent));
await p.screenshot({path:'rg.png'});
console.log(JSON.stringify({errs,med,hard:Object.keys(hard.cats).length,reveal},null,0));await b.close();})();
