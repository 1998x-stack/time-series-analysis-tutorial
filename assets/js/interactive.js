(()=>{
'use strict';
const labs=document.querySelectorAll('[data-lab]');
if(!labs.length)return;
function data(kind,v){
 if(kind==='rho')return {values:Array.from({length:12},(_,k)=>v**(k+1)),text:'理论相关：ρ(k)='+v.toFixed(2)+'^k。第 1 阶相关 = '+v.toFixed(3)};
 if(kind==='period')return {values:Array.from({length:24},(_,k)=>Math.sin(2*Math.PI*k/v)),text:'合成周期 P='+v.toFixed(0)+'，频率 f='+(1/v).toFixed(5)+' 周期/期。'};
 if(kind==='phi')return {values:Array.from({length:12},(_,k)=>v**k),text:'脉冲响应 ψ₀=1，ψ₁='+v.toFixed(3)+'，ψ₂='+(v*v).toFixed(4)};
 if(kind==='theta')return {values:[v/(1+v*v),0,0,0,0,0,0,0,0],text:'理论 ρ₁='+(v/(1+v*v)).toFixed(4)+'；'+(Math.abs(v)<1?'可逆（|θ|<1）':Math.abs(v)<=1.00001?'临界边界 |θ|=1，非严格可逆':'不可逆（|θ|>1）')};
 if(kind==='arma')return {values:Array.from({length:12},(_,k)=>k===0?1:(v+.35)*v**(k-1)),text:'θ=0.35，ψ₁='+(v+.35).toFixed(4)+'，ψ₂='+((v+.35)*v).toFixed(4)};
 if(kind==='diff'){
  const d=Math.round(v);
  if(d===0)return {values:Array.from({length:9},()=>0.99),text:'d=0：随机游走水平的理论自相关在各滞后都接近 1，几乎不衰减，需要差分。'};
  if(d===1)return {values:[1,0,0,0,0,0,0,0,0],text:'d=1：Δy_t=ε_t 是白噪声，除 ρ(0)=1 外自相关理论值为 0。'};
  return {values:[1,-0.5,0,0,0,0,0,0,0],text:'d=2：Δ²y_t=(1−B)ε_t 是 θ=−1 的 MA(1)，ρ(1)=−0.5，这是过度差分的典型信号。'};
 }
 if(kind==='season'){
  const s=Math.round(v);
  const values=Array.from({length:24},(_,k)=>k===0?1:(k%s===0?0.62:0));
  return {values,text:'季节周期 s='+s+'：自相关在滞后 '+s+'、'+(2*s)+'（周期的整数倍）出现峰，这种远程依赖是普通 ARMA 直接拟合困难的。'};
 }
 return {values:[],text:''};
}
for(const root of labs){
 const slider=root.querySelector('[data-lab-input]');
 const output=root.querySelector('[data-lab-output]');
 const note=root.querySelector('[data-lab-description]');
 const chart=root.querySelector('[data-lab-bars]');
 if(!slider||!output||!note||!chart)continue;
 const kind=root.getAttribute('data-lab');
 const update=()=>{
    const v=Number(slider.value);
    if(!Number.isFinite(v))return;
    const result=data(kind,v);
    const display=kind==='period'||kind==='diff'||kind==='season'?String(Math.round(v)):v.toFixed(2);
    output.value=display;output.textContent=display;
    note.textContent=result.text;
    chart.replaceChildren();
    chart.setAttribute('role','img');chart.setAttribute('aria-label',result.text);
    chart.style.setProperty('--bars',String(result.values.length));
    for(let k=0;k<result.values.length;k++){
       const num=result.values[k];
       const item=document.createElement('div');item.className='mini-bar';
       const bar=document.createElement('span');bar.className='mini-column '+(num<0?'negative':'positive');
       bar.style.height=Math.max(1,Math.round(Math.min(1,Math.abs(num))*46))+'%';
       bar.title='位置 '+k+'，数值 '+num.toFixed(4);
       const index=document.createElement('span');index.className='mini-index';
       index.textContent=kind==='period'?String(k+1):String(k);
       item.append(bar,index);chart.append(item);
    }
 };
 slider.addEventListener('input',update);
 update();
}
})();