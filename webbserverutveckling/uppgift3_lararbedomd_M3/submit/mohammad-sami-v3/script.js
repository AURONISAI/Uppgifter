// script.js - M3 v3
// Sami

// produkter
var produkter = [
  { id:"8805", namn:"Storm Puffer", pris:2999, beskr:"Vadderad puffer-jacka. Vindtat och varm.",
    farger:[
      { kod:"beige",       namn:"Beige",         hex:"#d8c8a8", bild:"assets/produkter/8805_beige.jpg" },
      { kod:"beige_black", namn:"Beige & Svart", hex:"#3a3a3a", bild:"assets/produkter/8805_beige_black.jpg" },
      { kod:"black",       namn:"Svart",         hex:"#111",    bild:"assets/produkter/8805_black.jpg" }
    ]},
  { id:"F0357", namn:"Edda Long", pris:3499, beskr:"Lang trenchcoat. Tidlos.",
    farger:[
      { kod:"black",       namn:"Svart",        hex:"#111",    bild:"assets/produkter/F0357_black.jpg" },
      { kod:"brown",       namn:"Brun",         hex:"#6b4423", bild:"assets/produkter/F0357_brown.jpg" },
      { kod:"brown_black", namn:"Brun & Svart", hex:"#3a2a18", bild:"assets/produkter/F0357_brown_black.jpg" }
    ]},
  { id:"F0445", namn:"Inci Coat", pris:2499, beskr:"Var bestseller. Vattentat och varm.",
    farger:[
      { kod:"beige",       namn:"Beige",         hex:"#d8c8a8", bild:"assets/produkter/F0445_beige.jpg" },
      { kod:"beige_brown", namn:"Beige & Brun",  hex:"#a07a4a", bild:"assets/produkter/F0445_beige_brown.jpg" },
      { kod:"black",       namn:"Svart",         hex:"#111",    bild:"assets/produkter/F0445_black.jpg" },
      { kod:"black_beige", namn:"Svart & Beige", hex:"#3a3a3a", bild:"assets/produkter/F0445_black_beige.jpg" },
      { kod:"brown",       namn:"Brun",          hex:"#6b4423", bild:"assets/produkter/F0445_brown.jpg" }
    ]},
  { id:"F0473", namn:"Aurora Coat", pris:2799, beskr:"Modern oversize.",
    farger:[
      { kod:"beige",       namn:"Beige",         hex:"#d8c8a8", bild:"assets/produkter/F0473_beige.jpg" },
      { kod:"beige_brown", namn:"Beige & Brun",  hex:"#a07a4a", bild:"assets/produkter/F0473_beige_brown.jpg" },
      { kod:"black",       namn:"Svart",         hex:"#111",    bild:"assets/produkter/F0473_black.jpg" },
      { kod:"black_beige", namn:"Svart & Beige", hex:"#3a3a3a", bild:"assets/produkter/F0473_black_beige.jpg" },
      { kod:"brown",       namn:"Brun",          hex:"#6b4423", bild:"assets/produkter/F0473_brown.jpg" }
    ]},
  { id:"F0474", namn:"Forest Bomber", pris:1899, beskr:"Bomberjacka for host.",
    farger:[
      { kod:"beige",       namn:"Beige",         hex:"#d8c8a8", bild:"assets/produkter/F0474_beige.jpg" },
      { kod:"beige_khaki", namn:"Beige & Khaki", hex:"#7a8458", bild:"assets/produkter/F0474_beige_khaki.jpg" },
      { kod:"khaki",       namn:"Khaki",         hex:"#5a6438", bild:"assets/produkter/F0474_khaki.jpg" }
    ]},
  { id:"L01", namn:"Nordic Light", pris:1599, beskr:"Lattvikt-jacka.",
    farger:[
      { kod:"black", namn:"Svart", hex:"#111",    bild:"assets/produkter/L01_black.jpg" },
      { kod:"green", namn:"Gron",  hex:"#3e6b3a", bild:"assets/produkter/L01_green.jpg" }
    ]}
];


// toast
function notis(text){
  var t = document.getElementById("toast");
  t.textContent = text;
  t.classList.add("visa");
  setTimeout(function(){ t.classList.remove("visa") }, 2200);
}


// tema
var temaBtn = document.getElementById("tema-btn");
if(localStorage.getItem("tema") == "morkt"){
  document.body.classList.add("morkt");
  temaBtn.setAttribute("aria-pressed","true");
}
temaBtn.onclick = function(){
  document.body.classList.toggle("morkt");
  var morkt = document.body.classList.contains("morkt");
  temaBtn.setAttribute("aria-pressed", morkt ? "true" : "false");
  localStorage.setItem("tema", morkt ? "morkt" : "ljust");
};


// accent farg
var fargPick = document.getElementById("farg-pick");
function satFarg(hex){
  document.documentElement.style.setProperty("--accent", hex);
  document.documentElement.style.setProperty("--mjuk", hex + "55");
}
if(localStorage.getItem("accent")){
  fargPick.value = localStorage.getItem("accent");
  satFarg(fargPick.value);
}
fargPick.oninput = function(){
  satFarg(fargPick.value);
  localStorage.setItem("accent", fargPick.value);
};
document.getElementById("aterstall-farg").onclick = function(){
  document.documentElement.style.removeProperty("--accent");
  document.documentElement.style.removeProperty("--mjuk");
  fargPick.value = "#82a31a";
  localStorage.removeItem("accent");
  notis("Aterstalld");
};


// katalog
var katalogYta = document.getElementById("katalog-yta");
var filterFarg = document.getElementById("filter-farg");
var sortera    = document.getElementById("sortera");
var antalInfo  = document.getElementById("antal-info");

function ritaKatalog(){
  var lista = produkter.slice();

  // filter
  if(filterFarg.value != "alla"){
    lista = lista.filter(function(p){
      for(var i=0; i<p.farger.length; i++){
        if(p.farger[i].kod.indexOf(filterFarg.value) > -1) return true;
      }
      return false;
    });
  }

  // sort
  if(sortera.value == "pris-upp") lista.sort(function(a,b){ return a.pris - b.pris });
  if(sortera.value == "pris-ner") lista.sort(function(a,b){ return b.pris - a.pris });
  if(sortera.value == "namn")     lista.sort(function(a,b){ return a.namn.localeCompare(b.namn) });

  katalogYta.innerHTML = "";
  for(var i=0; i<lista.length; i++){
    katalogYta.appendChild(byggKort(lista[i]));
  }
  antalInfo.textContent = lista.length + " av " + produkter.length;
}

function byggKort(p){
  var v = p.farger[0];
  var cirklar = "";
  for(var i=0; i<p.farger.length; i++){
    cirklar += '<span class="cirkel" style="background:' + p.farger[i].hex + '" title="' + p.farger[i].namn + '"></span>';
  }
  var div = document.createElement("div");
  div.className = "kort";
  div.setAttribute("role","listitem");
  div.setAttribute("tabindex","0");
  div.setAttribute("aria-label", p.namn + " " + p.pris + " kr");
  div.innerHTML =
    '<div class="bild"><img src="' + v.bild + '" alt="' + p.namn + '" loading="lazy"></div>' +
    '<div class="info">' +
      '<span class="titel">' + p.namn + '</span>' +
      '<span class="sku">art. ' + p.id + '</span>' +
      '<span class="pris">' + p.pris + ' kr</span>' +
      '<div class="farger">' + cirklar + '</div>' +
    '</div>';
  div.onclick = function(){ oppnaModal(p) };
  div.onkeydown = function(e){
    if(e.key == "Enter" || e.key == " "){ e.preventDefault(); oppnaModal(p) }
  };
  return div;
}

filterFarg.onchange = ritaKatalog;
sortera.onchange    = ritaKatalog;
ritaKatalog();


// modal
var modal       = document.getElementById("modal");
var modalBild   = document.getElementById("modal-bild");
var modalNamn   = document.getElementById("modal-namn");
var modalBeskr  = document.getElementById("modal-beskrivning");
var modalPris   = document.getElementById("modal-pris");
var modalFarger = document.getElementById("modal-fargvalj");
var aktiv = null;
var aktivVariant = null;

function oppnaModal(p){
  aktiv = p;
  aktivVariant = p.farger[0];
  uppdateraModal();

  modalFarger.innerHTML = "";
  for(var i=0; i<p.farger.length; i++){
    (function(v){
      var b = document.createElement("button");
      b.className = "farg-knapp" + (v == aktivVariant ? " vald" : "");
      b.style.background = v.hex;
      b.title = v.namn;
      b.setAttribute("type","button");
      b.setAttribute("role","radio");
      b.setAttribute("aria-label", v.namn);
      b.onclick = function(){
        aktivVariant = v;
        var alla = modalFarger.querySelectorAll(".farg-knapp");
        for(var j=0; j<alla.length; j++) alla[j].classList.remove("vald");
        b.classList.add("vald");
        uppdateraModal();
      };
      modalFarger.appendChild(b);
    })(p.farger[i]);
  }

  modal.classList.add("oppen");
  modal.setAttribute("aria-hidden","false");
}

function uppdateraModal(){
  modalBild.src = aktivVariant.bild;
  modalBild.alt = aktiv.namn + " " + aktivVariant.namn;
  modalNamn.textContent = aktiv.namn + " - " + aktivVariant.namn;
  modalBeskr.textContent = aktiv.beskr;
  modalPris.textContent = aktiv.pris + " kr";
}

function stangModal(){
  modal.classList.remove("oppen");
  modal.setAttribute("aria-hidden","true");
}

document.getElementById("modal-stang").onclick = stangModal;
modal.onclick = function(e){ if(e.target == modal) stangModal() };
document.onkeydown = function(e){
  if(e.key == "Escape" && modal.classList.contains("oppen")) stangModal();
};

document.getElementById("modal-lagg-till").onclick = function(){
  if(!aktiv) return;
  laggTill(aktiv, aktivVariant);
  stangModal();
};


// onskelista
var onskeYta = document.getElementById("onske-yta");
var raknare  = document.getElementById("raknare");
var varukorg = document.getElementById("varukorg-info");

function uppdateraRaknare(){
  var n = onskeYta.querySelectorAll(".onske-kort").length;
  raknare.textContent = n + " jackor";
  varukorg.textContent = n + " i listan";
  if(n == 0 && !onskeYta.querySelector(".tom-text")){
    var p = document.createElement("p");
    p.className = "tom-text";
    p.textContent = "Tom. Lagg till en jacka fran katalogen.";
    onskeYta.appendChild(p);
  }
  if(n > 0){
    var t = onskeYta.querySelector(".tom-text");
    if(t) t.remove();
  }
}

function laggTill(p, v){
  var t = onskeYta.querySelector(".tom-text");
  if(t) t.remove();

  var k = document.createElement("div");
  k.className = "onske-kort";
  k.setAttribute("tabindex","0");
  k.setAttribute("aria-label", p.namn + " " + v.namn);
  k.dataset.id = p.id;
  k.dataset.kod = v.kod;
  k.innerHTML =
    '<img src="' + v.bild + '" alt="' + p.namn + '">' +
    '<div class="info">' +
      '<span class="titel">' + p.namn + '</span>' +
      '<span class="pris-mini">' + v.namn + ' - ' + p.pris + ' kr</span>' +
    '</div>';
  function taBort(){
    k.remove();
    spara();
    notis(p.namn + " togs bort");
  }
  k.onclick = taBort;
  k.onkeydown = function(e){
    if(e.key == "Enter" || e.key == " " || e.key == "Delete"){ e.preventDefault(); taBort() }
  };
  onskeYta.appendChild(k);
  spara();
  notis(p.namn + " tillagd");
}

function spara(){
  var arr = [];
  var alla = onskeYta.querySelectorAll(".onske-kort");
  for(var i=0; i<alla.length; i++){
    arr.push({ id: alla[i].dataset.id, kod: alla[i].dataset.kod });
  }
  localStorage.setItem("onskelista-v3", JSON.stringify(arr));
  uppdateraRaknare();
}

function ladda(){
  var s = localStorage.getItem("onskelista-v3");
  if(!s){ uppdateraRaknare(); return }
  var arr = JSON.parse(s);
  for(var i=0; i<arr.length; i++){
    var p = null, v = null;
    for(var j=0; j<produkter.length; j++) if(produkter[j].id == arr[i].id) p = produkter[j];
    if(!p) continue;
    for(var j=0; j<p.farger.length; j++) if(p.farger[j].kod == arr[i].kod) v = p.farger[j];
    if(!v) continue;
    laggTill(p, v);
  }
  // ta bort de "tillagd" toasterna som spammats
}
ladda();

document.getElementById("rensa-rutor").onclick = function(){
  var alla = onskeYta.querySelectorAll(".onske-kort");
  for(var i=0; i<alla.length; i++) alla[i].remove();
  localStorage.removeItem("onskelista-v3");
  uppdateraRaknare();
  notis("Onskelistan tomdes");
};


// vader
document.getElementById("hamta-vader").onclick = function(){
  var yta = document.getElementById("vader-yta");
  yta.textContent = "Hamtar...";
  fetch("https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.07&current=temperature_2m,wind_speed_10m")
    .then(function(r){ return r.json() })
    .then(function(d){
      var t = d.current.temperature_2m;
      var v = d.current.wind_speed_10m;
      var tipsId = "L01";
      var tipsText = "Nordic Light - lattvikt for varma dagar.";
      if(t < 0)       { tipsId = "8805";  tipsText = "Storm Puffer - vadderad och vindtat." }
      else if(t < 8)  { tipsId = "F0445"; tipsText = "Inci Coat - vattentat och varm." }
      else if(t < 15) { tipsId = "F0473"; tipsText = "Aurora Coat - oversize for hostvader." }
      else if(t < 22) { tipsId = "F0474"; tipsText = "Forest Bomber - lattare for milda dagar." }

      var bild = "";
      for(var i=0; i<produkter.length; i++){
        if(produkter[i].id == tipsId){ bild = produkter[i].farger[0].bild; break }
      }
      yta.innerHTML =
        '<div><strong>' + t + '°C</strong> i Stockholm, vind ' + v + ' m/s.<br>Tips: ' + tipsText + '</div>' +
        (bild ? '<img src="' + bild + '" alt="Tips">' : '');
    })
    .catch(function(){ yta.textContent = "Kunde inte hamta vader." });
};


// fakta
document.getElementById("hamta-fakta").onclick = function(){
  var p = document.getElementById("fakta-text");
  p.textContent = "Hamtar...";
  fetch("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    .then(function(r){ return r.json() })
    .then(function(d){ p.textContent = "Visste du: " + d.text })
    .catch(function(){ p.textContent = "Kunde inte hamta tips." });
};
