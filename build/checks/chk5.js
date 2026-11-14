const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.cwd()+'/zeppelin-grid.html');
const r=await p.evaluate(()=>{ // generate many grids by clicking random and record min answers
  let bad=0, fallbacks=0, cats={}, schools={};
  for(let i=0;i<300;i++){ document.getElementById('random').click();
    const heads=[...document.querySelectorAll('.head')].map(x=>x.firstChild.textContent);
    heads.forEach(h=>cats[h]=(cats[h]||0)+1);
    [...document.querySelectorAll('.rowhead')].forEach(x=>schools[x.title]=(schools[x.title]||0)+1);
  } return {cats,schools};});
await p.click('#cell-0');await p.fill('#q','the');await p.waitForTimeout(100);
const list=await p.$$eval('#results button',x=>x.map(b=>b.textContent));
await p.screenshot({path:'lz.png'});
console.log(JSON.stringify({errs,r,list}));await b.close();})();
