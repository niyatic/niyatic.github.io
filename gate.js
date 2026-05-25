/* HyperAPI Pages gate — obfuscation-grade JS check; NOT a real auth boundary.
 * Anyone with the URL can curl raw HTML and bypass.
 * Real auth requires private-repo Pages OR Cloudflare Access in front.
 * Password hash below is SHA-256 of the chosen passphrase.
 * Updated 2026-05-25 — new passphrase + Hyperbots logo on gate UI.
 */
(function(){
  var EXPECTED='c70584534abeba13454b6fe26d4547dceddad67d1d9d33e701f445cb5bb56259';
  if(sessionStorage.getItem('hb_auth')===EXPECTED){return;}
  document.documentElement.style.visibility='hidden';
  document.addEventListener('DOMContentLoaded',function(){
    document.documentElement.innerHTML='<head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Hyperbots — content hub</title><style>'
    +'body{font:15px/1.55 "Rubik",-apple-system,BlinkMacSystemFont,system-ui,sans-serif;background:#F6F9F9;color:#211F26;padding:80px 24px;text-align:center;margin:0;-webkit-font-smoothing:antialiased}'
    +'.box{max-width:400px;margin:0 auto;background:#fff;border:1px solid #E2ECEE;border-radius:14px;padding:40px 32px 32px;box-shadow:0 2px 12px rgba(33,31,38,.08);border-left:5px solid #1B7DA7}'
    +'.logo{width:56px;height:56px;margin:0 auto 14px;display:block}'
    +'h1{font-size:20px;margin:0 0 4px;color:#07658D;font-weight:600;letter-spacing:-0.01em}'
    +'p.s{font-size:13px;color:#748081;margin:0 0 24px}'
    +'input{width:100%;padding:11px 14px;border:1px solid #BDDFEE;border-radius:8px;font-size:14px;margin-bottom:12px;outline:none;background:#F6F9F9;box-sizing:border-box;font-family:inherit}'
    +'input:focus{border-color:#1B7DA7;background:#fff}'
    +'button{width:100%;padding:11px;background:#1B7DA7;color:#fff;border:0;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;font-family:inherit}'
    +'button:hover{background:#07658D}'
    +'.err{color:#B42318;font-size:12.5px;margin-top:8px;min-height:16px}'
    +'.note{margin-top:18px;font-size:11.5px;color:#748081;line-height:1.5}'
    +'</style></head>'
    +'<body><div class="box">'
    +'<img class="logo" src="/assets/hyperbots-logo.svg" alt="Hyperbots" onerror="this.style.display=\'none\'"/>'
    +'<h1>Hyperbots content hub</h1><p class="s">Passphrase required</p>'
    +'<form id="f"><input id="p" type="password" placeholder="passphrase" autofocus autocomplete="off"/>'
    +'<button type="submit">unlock</button><div class="err" id="e"></div></form>'
    +'<div class="note">Session-scoped; cleared on browser close.</div></div></body>';
    var f=document.getElementById('f');
    f.addEventListener('submit',async function(ev){
      ev.preventDefault();
      var v=document.getElementById('p').value;
      var ab=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(v));
      var hh=Array.from(new Uint8Array(ab)).map(function(x){return x.toString(16).padStart(2,'0');}).join('');
      if(hh===EXPECTED){sessionStorage.setItem('hb_auth',EXPECTED);location.reload();}
      else{document.getElementById('e').textContent='wrong passphrase';document.getElementById('p').select();}
    });
    document.documentElement.style.visibility='visible';
  });
})();
