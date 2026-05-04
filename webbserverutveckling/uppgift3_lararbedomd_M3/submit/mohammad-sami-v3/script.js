// script.js - Sami M3

// mina jackor med farger
var jackor = [
  { id:"8805",  namn:"Storm Puffer",  pris:2999, beskr:"Vadderad puffer. Vindtat och varm.", farger:[
    {kod:"beige",namn:"Beige",hex:"#d8c8a8",bild:"assets/produkter/8805_beige.jpg"},
    {kod:"beige_black",namn:"Beige & Svart",hex:"#3a3a3a",bild:"assets/produkter/8805_beige_black.jpg"},
    {kod:"black",namn:"Svart",hex:"#111",bild:"assets/produkter/8805_black.jpg"} ]},
  { id:"F0357", namn:"Edda Long",     pris:3499, beskr:"Lang trenchcoat, tidlos.", farger:[
    {kod:"black",namn:"Svart",hex:"#111",bild:"assets/produkter/F0357_black.jpg"},
    {kod:"brown",namn:"Brun",hex:"#6b4423",bild:"assets/produkter/F0357_brown.jpg"},
    {kod:"brown_black",namn:"Brun & Svart",hex:"#3a2a18",bild:"assets/produkter/F0357_brown_black.jpg"} ]},
  { id:"F0445", namn:"Inci Coat",     pris:2499, beskr:"Var bestseller. Vattentat.", farger:[
    {kod:"beige",namn:"Beige",hex:"#d8c8a8",bild:"assets/produkter/F0445_beige.jpg"},
    {kod:"beige_brown",namn:"Beige & Brun",hex:"#a07a4a",bild:"assets/produkter/F0445_beige_brown.jpg"},
    {kod:"black",namn:"Svart",hex:"#111",bild:"assets/produkter/F0445_black.jpg"},
    {kod:"black_beige",namn:"Svart & Beige",hex:"#3a3a3a",bild:"assets/produkter/F0445_black_beige.jpg"},
    {kod:"brown",namn:"Brun",hex:"#6b4423",bild:"assets/produkter/F0445_brown.jpg"} ]},
  { id:"F0473", namn:"Aurora Coat",   pris:2799, beskr:"Modern oversize.", farger:[
    {kod:"beige",namn:"Beige",hex:"#d8c8a8",bild:"assets/produkter/F0473_beige.jpg"},
    {kod:"beige_brown",namn:"Beige & Brun",hex:"#a07a4a",bild:"assets/produkter/F0473_beige_brown.jpg"},
    {kod:"black",namn:"Svart",hex:"#111",bild:"assets/produkter/F0473_black.jpg"},
    {kod:"black_beige",namn:"Svart & Beige",hex:"#3a3a3a",bild:"assets/produkter/F0473_black_beige.jpg"},
    {kod:"brown",namn:"Brun",hex:"#6b4423",bild:"assets/produkter/F0473_brown.jpg"} ]},
  { id:"F0474", namn:"Forest Bomber", pris:1899, beskr:"Bomberjacka.", farger:[
    {kod:"beige",namn:"Beige",hex:"#d8c8a8",bild:"assets/produkter/F0474_beige.jpg"},
    {kod:"beige_khaki",namn:"Beige & Khaki",hex:"#7a8458",bild:"assets/produkter/F0474_beige_khaki.jpg"},
    {kod:"khaki",namn:"Khaki",hex:"#5a6438",bild:"assets/produkter/F0474_khaki.jpg"} ]},
  { id:"L01",   namn:"Nordic Light",  pris:1599, beskr:"Lattvikt-jacka.", farger:[
    {kod:"black",namn:"Svart",hex:"#111",bild:"assets/produkter/L01_black.jpg"},
    {kod:"green",namn:"Gron",hex:"#3e6b3a",bild:"assets/produkter/L01_green.jpg"} ]}
];


// hamta saker fran sidan
var katalog = document.getElementById("katalog-yta");
var filter = document.getElementById("filter-farg");
var sort = document.getElementById("sortera");
var antalText = document.getElementById("antal-info");
var modal = document.getElementById("modal");
var mBild = document.getElementById("modal-bild");
var mNamn = document.getElementById("modal-namn");
var mBeskr = document.getElementById("modal-beskrivning");
var mPris = document.getElementById("modal-pris");
var mFargvalj = document.getElementById("modal-fargvalj");
var onskeYta = document.getElementById("onske-yta");
var raknare = document.getElementById("raknare");
var varukorg = document.getElementById("varukorg-info");
var toast = document.getElementById("toast");


// hitta jacka pa id
function hittaJacka(id){
  for(var i=0; i<jackor.length; i++){
    if(jackor[i].id == id){ return jackor[i] }
  }
  return null;
}


// rita katalogen
function ritaKatalog(){
  var lista = jackor.slice(); // kopia

  // filter
  if(filter.value != "alla"){
    var ny = [];
    for(var i=0; i<lista.length; i++){
      for(var j=0; j<lista[i].farger.length; j++){
        if(lista[i].farger[j].kod.indexOf(filter.value) > -1){
          ny.push(lista[i]);
          break;
        }
      }
    }
    lista = ny;
  }

  // sortera
  if(sort.value == "pris-upp") lista.sort(function(a,b){ return a.pris - b.pris });
  if(sort.value == "pris-ner") lista.sort(function(a,b){ return b.pris - a.pris });
  if(sort.value == "namn") lista.sort(function(a,b){ return a.namn < b.namn ? -1 : 1 });

  // bygg html
  var html = "";
  for(var i=0; i<lista.length; i++){
    var p = lista[i];
    var v = p.farger[0];
    var cirklar = "";
    for(var k=0; k<p.farger.length; k++){
      cirklar += '<span class="cirkel" style="background:' + p.farger[k].hex + '"></span>';
    }
    html += '<div class="kort" tabindex="0" role="listitem" data-id="' + p.id + '">' +
      '<div class="bild"><img src="' + v.bild + '" alt="' + p.namn + '"></div>' +
      '<div class="info">' +
        '<span class="titel">' + p.namn + '</span>' +
        '<span class="sku">art. ' + p.id + '</span>' +
        '<span class="pris">' + p.pris + ' kr</span>' +
        '<div class="farger">' + cirklar + '</div>' +
      '</div></div>';
  }
  katalog.innerHTML = html;
  antalText.textContent = lista.length + " av " + jackor.length;

  // klick pa kort
  var alla = document.querySelectorAll(".kort");
  for(var i=0; i<alla.length; i++){
    alla[i].onclick = function(){ oppna(this.getAttribute("data-id")) };
    alla[i].onkeydown = function(e){
      if(e.key == "Enter") oppna(this.getAttribute("data-id"));
    };
  }
}


// MODAL
var aktivJacka = null;
var aktivFarg = null;

function oppna(id){
  aktivJacka = hittaJacka(id);
  aktivFarg = aktivJacka.farger[0];

  // bygg fargknappar
  var html = "";
  for(var i=0; i<aktivJacka.farger.length; i++){
    var f = aktivJacka.farger[i];
    var vald = (f == aktivFarg) ? " vald" : "";
    html += '<button type="button" class="farg-knapp' + vald + '" style="background:' + f.hex +
            '" title="' + f.namn + '" data-kod="' + f.kod + '"></button>';
  }
  mFargvalj.innerHTML = html;

  var knappar = document.querySelectorAll(".farg-knapp");
  for(var i=0; i<knappar.length; i++){
    knappar[i].onclick = bytFarg;
  }

  visaModal();
  modal.classList.add("oppen");
  modal.setAttribute("aria-hidden", "false");
}

function bytFarg(){
  var kod = this.getAttribute("data-kod");
  for(var i=0; i<aktivJacka.farger.length; i++){
    if(aktivJacka.farger[i].kod == kod) aktivFarg = aktivJacka.farger[i];
  }
  var alla = document.querySelectorAll(".farg-knapp");
  for(var i=0; i<alla.length; i++) alla[i].classList.remove("vald");
  this.classList.add("vald");
  visaModal();
}

function visaModal(){
  mBild.src = aktivFarg.bild;
  mBild.alt = aktivJacka.namn + " " + aktivFarg.namn;
  mNamn.textContent = aktivJacka.namn + " - " + aktivFarg.namn;
  mBeskr.textContent = aktivJacka.beskr;
  mPris.textContent = aktivJacka.pris + " kr";
}

function stang(){
  modal.classList.remove("oppen");
  modal.setAttribute("aria-hidden", "true");
}

document.getElementById("modal-stang").onclick = stang;
modal.onclick = function(e){ if(e.target == modal) stang() };
document.onkeydown = function(e){ if(e.key == "Escape") stang() };

document.getElementById("modal-lagg-till").onclick = function(){
  if(aktivJacka == null) return;
  laggTill(aktivJacka, aktivFarg);
  stang();
};


// ONSKELISTA
function laggTill(p, f){
  var tom = onskeYta.querySelector(".tom-text");
  if(tom != null) tom.remove();

  var k = document.createElement("div");
  k.className = "onske-kort";
  k.setAttribute("tabindex", "0");
  k.setAttribute("data-id", p.id);
  k.setAttribute("data-kod", f.kod);
  k.innerHTML = '<img src="' + f.bild + '" alt="' + p.namn + '">' +
    '<div class="info"><span class="titel">' + p.namn + '</span>' +
    '<span class="pris-mini">' + f.namn + ' - ' + p.pris + ' kr</span></div>';

  function taBort(){ k.remove(); spara(); visaToast(p.namn + " togs bort") }
  k.onclick = taBort;
  k.onkeydown = function(e){ if(e.key == "Enter" || e.key == "Delete") taBort() };

  onskeYta.appendChild(k);
  spara();
  visaToast(p.namn + " tillagd");
}

function spara(){
  var alla = document.querySelectorAll(".onske-kort");
  var arr = [];
  for(var i=0; i<alla.length; i++){
    arr.push({ id: alla[i].getAttribute("data-id"), kod: alla[i].getAttribute("data-kod") });
  }
  localStorage.setItem("onskelista", JSON.stringify(arr));
  uppdateraRaknare();
}

function ladda(){
  var data = localStorage.getItem("onskelista");
  if(data == null){ uppdateraRaknare(); return }
  var arr = JSON.parse(data);
  for(var i=0; i<arr.length; i++){
    var p = hittaJacka(arr[i].id);
    if(p == null) continue;
    for(var j=0; j<p.farger.length; j++){
      if(p.farger[j].kod == arr[i].kod){ laggTill(p, p.farger[j]); break }
    }
  }
}

function uppdateraRaknare(){
  var n = document.querySelectorAll(".onske-kort").length;
  raknare.textContent = n + " jackor";
  varukorg.textContent = n + " i listan";
  if(n == 0 && onskeYta.querySelector(".tom-text") == null){
    onskeYta.innerHTML = '<p class="tom-text">Tom. Lagg till en jacka fran katalogen.</p>';
  }
}

document.getElementById("rensa-rutor").onclick = function(){
  onskeYta.innerHTML = "";
  localStorage.removeItem("onskelista");
  uppdateraRaknare();
  visaToast("Onskelistan tomdes");
};


// TOAST
var toastTimer;
function visaToast(text){
  toast.textContent = text;
  toast.classList.add("visa");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(function(){ toast.classList.remove("visa") }, 2000);
}


// TEMA
var temaBtn = document.getElementById("tema-btn");
if(localStorage.getItem("tema") == "morkt"){
  document.body.classList.add("morkt");
  temaBtn.setAttribute("aria-pressed", "true");
}
temaBtn.onclick = function(){
  document.body.classList.toggle("morkt");
  var morkt = document.body.classList.contains("morkt");
  localStorage.setItem("tema", morkt ? "morkt" : "ljust");
  temaBtn.setAttribute("aria-pressed", morkt ? "true" : "false");
};


// FARG-picker
var fargPick = document.getElementById("farg-pick");
function satFarg(hex){
  document.documentElement.style.setProperty("--accent", hex);
  document.documentElement.style.setProperty("--mjuk", hex + "55");
}
if(localStorage.getItem("accent") != null){
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
  visaToast("Aterstalld");
};


// VADER (fetch 1)
document.getElementById("hamta-vader").onclick = function(){
  var yta = document.getElementById("vader-yta");
  yta.textContent = "Hamtar...";
  fetch("https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.07&current=temperature_2m,wind_speed_10m")
    .then(function(s){ return s.json() })
    .then(function(d){
      var t = d.current.temperature_2m;
      var v = d.current.wind_speed_10m;
      var id = "L01", text = "Nordic Light - lattvikt for varma dagar";
      if(t < 0)       { id = "8805";  text = "Storm Puffer - vadderad och vindtat" }
      else if(t < 8)  { id = "F0445"; text = "Inci Coat - vattentat och varm" }
      else if(t < 15) { id = "F0473"; text = "Aurora Coat - oversize for hostvader" }
      else if(t < 22) { id = "F0474"; text = "Forest Bomber - lattare for milda dagar" }
      var bild = hittaJacka(id).farger[0].bild;
      yta.innerHTML = '<div><strong>' + t + '°C</strong> i Stockholm, vind ' + v + ' m/s.<br>Tips: ' + text + '</div>' +
        '<img src="' + bild + '" alt="Tips">';
    })
    .catch(function(){ yta.textContent = "Kunde inte hamta vader." });
};


// FAKTA (fetch 2)
document.getElementById("hamta-fakta").onclick = function(){
  var p = document.getElementById("fakta-text");
  p.textContent = "Hamtar...";
  fetch("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    .then(function(s){ return s.json() })
    .then(function(d){ p.textContent = "Visste du: " + d.text })
    .catch(function(){ p.textContent = "Kunde inte hamta tips." });
};


// kor!
filter.onchange = ritaKatalog;
sort.onchange = ritaKatalog;
ritaKatalog();
ladda();
