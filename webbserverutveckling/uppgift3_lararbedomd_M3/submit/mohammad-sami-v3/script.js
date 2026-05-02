// script.js - M3 v3 Katalog - Sami
// Riktig produktkatalog med riktiga foton.
// DOM + Fetch + LocalStorage + tema + accentfarg + toast + modal + filter/sort.

// ============ PRODUKTDATA ============
// Varje produkt har flera fargvarianter. Bilder finns i assets/produkter/
var produkter = [
  {
    id: "8805",
    namn: "Storm Puffer",
    beskrivning: "Vadderad puffer-jacka i tva-fargs design. Vindtat ytterskikt och varm fyllning - perfekt for kalla dagar.",
    pris: 2999,
    varianter: [
      { farg:"Beige",        kod:"beige",       hex:"#d8c8a8", bild:"assets/produkter/8805_beige.jpg" },
      { farg:"Beige & Svart",kod:"beige_black", hex:"#3a3a3a", bild:"assets/produkter/8805_beige_black.jpg" },
      { farg:"Svart",        kod:"black",       hex:"#111111", bild:"assets/produkter/8805_black.jpg" }
    ]
  },
  {
    id: "F0357",
    namn: "Edda Long",
    beskrivning: "Lang, klassisk skarcoat med mjuk insida. En tidlos modell som hojer varje outfit.",
    pris: 3499,
    varianter: [
      { farg:"Svart",         kod:"black",       hex:"#111111", bild:"assets/produkter/F0357_black.jpg" },
      { farg:"Brun",          kod:"brown",       hex:"#6b4423", bild:"assets/produkter/F0357_brown.jpg" },
      { farg:"Brun & Svart",  kod:"brown_black", hex:"#3a2a18", bild:"assets/produkter/F0357_brown_black.jpg" }
    ]
  },
  {
    id: "F0445",
    namn: "Inci Coat",
    beskrivning: "Var bestseller. Vattentat och vindtat ytterskikt med varm foring. Finns i fem fargvarianter.",
    pris: 2499,
    varianter: [
      { farg:"Beige",        kod:"beige",       hex:"#d8c8a8", bild:"assets/produkter/F0445_beige.jpg" },
      { farg:"Beige & Brun", kod:"beige_brown", hex:"#a07a4a", bild:"assets/produkter/F0445_beige_brown.jpg" },
      { farg:"Svart",        kod:"black",       hex:"#111111", bild:"assets/produkter/F0445_black.jpg" },
      { farg:"Svart & Beige",kod:"black_beige", hex:"#3a3a3a", bild:"assets/produkter/F0445_black_beige.jpg" },
      { farg:"Brun",         kod:"brown",       hex:"#6b4423", bild:"assets/produkter/F0445_brown.jpg" }
    ]
  },
  {
    id: "F0473",
    namn: "Aurora Coat",
    beskrivning: "Modern oversize-snitt med struktur-tyg. Lika snygg uppknappt som ihop-knappt.",
    pris: 2799,
    varianter: [
      { farg:"Beige",         kod:"beige",       hex:"#d8c8a8", bild:"assets/produkter/F0473_beige.jpg" },
      { farg:"Beige & Brun",  kod:"beige_brown", hex:"#a07a4a", bild:"assets/produkter/F0473_beige_brown.jpg" },
      { farg:"Svart",         kod:"black",       hex:"#111111", bild:"assets/produkter/F0473_black.jpg" },
      { farg:"Svart & Beige", kod:"black_beige", hex:"#3a3a3a", bild:"assets/produkter/F0473_black_beige.jpg" },
      { farg:"Brun",          kod:"brown",       hex:"#6b4423", bild:"assets/produkter/F0473_brown.jpg" }
    ]
  },
  {
    id: "F0474",
    namn: "Forest Bomber",
    beskrivning: "Sportig bomberjacka i mjukt material. Lattare passform - perfekt for host och var.",
    pris: 1899,
    varianter: [
      { farg:"Beige",         kod:"beige",       hex:"#d8c8a8", bild:"assets/produkter/F0474_beige.jpg" },
      { farg:"Beige & Khaki", kod:"beige_khaki", hex:"#7a8458", bild:"assets/produkter/F0474_beige_khaki.jpg" },
      { farg:"Khaki",         kod:"khaki",       hex:"#5a6438", bild:"assets/produkter/F0474_khaki.jpg" }
    ]
  },
  {
    id: "L01",
    namn: "Nordic Light",
    beskrivning: "Lattvikt-jacka for milda dagar. Andningsbar och vattenavvisande - lat att vika ihop.",
    pris: 1599,
    varianter: [
      { farg:"Svart", kod:"black", hex:"#111111", bild:"assets/produkter/L01_black.jpg" },
      { farg:"Gron",  kod:"green", hex:"#3e6b3a", bild:"assets/produkter/L01_green.jpg" }
    ]
  }
];


// ============ TOAST ============
var toast = document.getElementById("toast");
var toastTimer;
function notis(text){
  if(!toast){ return }
  toast.textContent = text;
  toast.classList.add("visa");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(function(){ toast.classList.remove("visa") }, 2400);
}


// ============ TEMA ============
var temaBtn = document.getElementById("tema-btn");
var morkt = false;
if(localStorage.getItem("tema") == "morkt"){
  document.body.classList.add("morkt");
  morkt = true;
}
if(temaBtn){
  if(morkt){ temaBtn.setAttribute("aria-pressed","true") }
  temaBtn.addEventListener("click", function(){
    morkt = !morkt;
    if(morkt){
      document.body.classList.add("morkt");
      temaBtn.setAttribute("aria-pressed","true");
      localStorage.setItem("tema","morkt");
    } else {
      document.body.classList.remove("morkt");
      temaBtn.setAttribute("aria-pressed","false");
      localStorage.setItem("tema","ljust");
    }
  });
}


// ============ ACCENT-FARG ============
var fargPick = document.getElementById("farg-pick");
var aterstall = document.getElementById("aterstall-farg");

function satFarg(hex){
  document.documentElement.style.setProperty("--accent", hex);
  document.documentElement.style.setProperty("--accent-mjuk", hex + "55");
}
var sparadFarg = localStorage.getItem("accent");
if(sparadFarg){ satFarg(sparadFarg); if(fargPick){ fargPick.value = sparadFarg } }

if(fargPick){
  fargPick.addEventListener("input", function(){
    satFarg(fargPick.value);
    localStorage.setItem("accent", fargPick.value);
  });
}
if(aterstall){
  aterstall.addEventListener("click", function(){
    document.documentElement.style.removeProperty("--accent");
    document.documentElement.style.removeProperty("--accent-mjuk");
    if(fargPick){ fargPick.value = "#82a31a" }
    localStorage.removeItem("accent");
    notis("Accentfarg aterstalld");
  });
}


// ============ KATALOG (filter + sort + render) ============
var katalogYta = document.getElementById("katalog-yta");
var filterFarg = document.getElementById("filter-farg");
var sortera   = document.getElementById("sortera");
var antalInfo = document.getElementById("antal-info");

function ritaKatalog(){
  var fargVal = filterFarg.value;
  var sortVal = sortera.value;

  // klona och filtrera
  var lista = produkter.slice();
  if(fargVal != "alla"){
    lista = lista.filter(function(p){
      // produkten visas om nagon variant matchar fargen
      for(var i=0; i<p.varianter.length; i++){
        if(p.varianter[i].kod.indexOf(fargVal) > -1){ return true }
      }
      return false;
    });
  }

  // sortera
  if(sortVal == "pris-upp"){ lista.sort(function(a,b){ return a.pris - b.pris }) }
  if(sortVal == "pris-ner"){ lista.sort(function(a,b){ return b.pris - a.pris }) }
  if(sortVal == "namn"){     lista.sort(function(a,b){ return a.namn.localeCompare(b.namn) }) }

  katalogYta.innerHTML = "";
  for(var i=0; i<lista.length; i++){
    katalogYta.appendChild(byggProduktKort(lista[i], fargVal));
  }

  antalInfo.textContent = lista.length + " av " + produkter.length + " modeller";
}

function byggProduktKort(p, fargVal){
  // valj forsta variant som matchar filter (eller forsta annars)
  var huvudVariant = p.varianter[0];
  if(fargVal && fargVal != "alla"){
    for(var i=0; i<p.varianter.length; i++){
      if(p.varianter[i].kod.indexOf(fargVal) > -1){ huvudVariant = p.varianter[i]; break }
    }
  }

  var div = document.createElement("div");
  div.className = "produkt-kort";
  div.setAttribute("role","listitem");
  div.setAttribute("tabindex","0");
  div.setAttribute("aria-label", p.namn + ", fran " + p.pris + " kr, " + p.varianter.length + " fargvarianter, klicka for detaljer");

  var fargCirklar = "";
  for(var j=0; j<p.varianter.length; j++){
    fargCirklar += '<span class="cirkel" style="background:' + p.varianter[j].hex + '" title="' + p.varianter[j].farg + '"></span>';
  }

  div.innerHTML =
    '<div class="bild-yta">' +
      '<span class="markning">' + p.varianter.length + ' farger</span>' +
      '<img src="' + huvudVariant.bild + '" alt="' + p.namn + ' i farg ' + huvudVariant.farg + '" loading="lazy">' +
    '</div>' +
    '<div class="info">' +
      '<span class="titel">' + p.namn + '</span>' +
      '<span class="sku">art. ' + p.id + '</span>' +
      '<div class="farg-cirklar">' + fargCirklar + '</div>' +
      '<span class="pris">' + p.pris + ' kr</span>' +
    '</div>';

  div.addEventListener("click", function(){ oppnaModal(p, huvudVariant) });
  div.addEventListener("keydown", function(e){
    if(e.key == "Enter" || e.key == " "){ e.preventDefault(); oppnaModal(p, huvudVariant) }
  });

  return div;
}

filterFarg.addEventListener("change", ritaKatalog);
sortera.addEventListener("change", ritaKatalog);
ritaKatalog();


// ============ PRODUKTMODAL ============
var modal = document.getElementById("modal");
var modalBild = document.getElementById("modal-bild");
var modalNamn = document.getElementById("modal-namn");
var modalBeskr = document.getElementById("modal-beskrivning");
var modalPris = document.getElementById("modal-pris");
var modalFargvalj = document.getElementById("modal-fargvalj");
var modalLaggTill = document.getElementById("modal-lagg-till");
var modalStang = document.getElementById("modal-stang");

var aktivProdukt = null;
var aktivVariant = null;

function oppnaModal(p, startVariant){
  aktivProdukt = p;
  aktivVariant = startVariant || p.varianter[0];

  modalNamn.textContent = p.namn + " - " + aktivVariant.farg;
  modalBeskr.textContent = p.beskrivning;
  modalPris.textContent = p.pris + " kr";
  modalBild.src = aktivVariant.bild;
  modalBild.alt = p.namn + " i farg " + aktivVariant.farg;

  // bygg fargknappar
  modalFargvalj.innerHTML = "";
  for(var i=0; i<p.varianter.length; i++){
    (function(v){
      var b = document.createElement("button");
      b.className = "farg-knapp" + (v.kod == aktivVariant.kod ? " vald" : "");
      b.style.background = v.hex;
      b.setAttribute("type","button");
      b.setAttribute("role","radio");
      b.setAttribute("aria-checked", v.kod == aktivVariant.kod ? "true" : "false");
      b.setAttribute("aria-label", v.farg);
      b.title = v.farg;
      b.addEventListener("click", function(){ valjVariant(v) });
      modalFargvalj.appendChild(b);
    })(p.varianter[i]);
  }

  modal.classList.add("oppen");
  modal.setAttribute("aria-hidden","false");
  document.body.style.overflow = "hidden";
  modalStang.focus();
}

function valjVariant(v){
  aktivVariant = v;
  modalBild.src = v.bild;
  modalBild.alt = aktivProdukt.namn + " i farg " + v.farg;
  modalNamn.textContent = aktivProdukt.namn + " - " + v.farg;
  // uppdatera knappar
  var alla = modalFargvalj.querySelectorAll(".farg-knapp");
  for(var i=0; i<alla.length; i++){
    alla[i].classList.remove("vald");
    alla[i].setAttribute("aria-checked","false");
  }
  // markera ratt knapp
  var index = aktivProdukt.varianter.indexOf(v);
  if(index >= 0){
    alla[index].classList.add("vald");
    alla[index].setAttribute("aria-checked","true");
  }
}

function stangModal(){
  modal.classList.remove("oppen");
  modal.setAttribute("aria-hidden","true");
  document.body.style.overflow = "";
}

modalStang.addEventListener("click", stangModal);
modal.addEventListener("click", function(e){
  if(e.target == modal){ stangModal() }
});
document.addEventListener("keydown", function(e){
  if(e.key == "Escape" && modal.classList.contains("oppen")){ stangModal() }
});

modalLaggTill.addEventListener("click", function(){
  if(!aktivProdukt || !aktivVariant){ return }
  laggTillIOnskelista(aktivProdukt, aktivVariant);
  stangModal();
});


// ============ ONSKELISTA ============
var onskeYta = document.getElementById("onske-yta");
var rensaRutorBtn = document.getElementById("rensa-rutor");
var raknare = document.getElementById("raknare");
var varukorgInfo = document.getElementById("varukorg-info");

function uppdateraRaknare(){
  // bortse fran tom-text om den finns
  var n = onskeYta.querySelectorAll(".onske-kort").length;
  raknare.textContent = n + " jackor";
  varukorgInfo.textContent = n + " i onskelistan";
  // tom-text
  if(n == 0){
    if(!onskeYta.querySelector(".tom-text")){
      var p = document.createElement("p");
      p.className = "tom-text";
      p.textContent = "Din onskelista ar tom. Lagg till en jacka fran katalogen ovan.";
      onskeYta.appendChild(p);
    }
  } else {
    var t = onskeYta.querySelector(".tom-text");
    if(t){ t.remove() }
  }
}

function laggTillIOnskelista(p, v){
  // skapa kort
  var k = document.createElement("div");
  k.className = "onske-kort";
  k.setAttribute("role","listitem");
  k.setAttribute("tabindex","0");
  k.setAttribute("aria-label", p.namn + " " + v.farg + " - " + p.pris + " kr - tryck Enter for att ta bort");

  k.dataset.id = p.id;
  k.dataset.kod = v.kod;

  k.innerHTML =
    '<img src="' + v.bild + '" alt="' + p.namn + ' i ' + v.farg + '">' +
    '<span class="ta-bort">Ta bort</span>' +
    '<div class="info">' +
      '<span class="titel">' + p.namn + '</span>' +
      '<span class="pris-mini">' + v.farg + ' &middot; ' + p.pris + ' kr</span>' +
    '</div>';

  function taBort(){
    k.remove();
    sparaOnskelista();
    notis(p.namn + " togs bort");
  }
  k.addEventListener("click", taBort);
  k.addEventListener("keydown", function(e){
    if(e.key == "Enter" || e.key == " " || e.key == "Delete"){
      e.preventDefault(); taBort();
    }
  });

  // ta bort tom-text om den finns
  var t = onskeYta.querySelector(".tom-text");
  if(t){ t.remove() }

  onskeYta.appendChild(k);
  sparaOnskelista();
  notis(p.namn + " (" + v.farg + ") tillagd");
}

function sparaOnskelista(){
  var alla = onskeYta.querySelectorAll(".onske-kort");
  var arr = [];
  for(var i=0; i<alla.length; i++){
    arr.push({ id: alla[i].dataset.id, kod: alla[i].dataset.kod });
  }
  localStorage.setItem("onskelista-v3", JSON.stringify(arr));
  uppdateraRaknare();
}

function laddaOnskelista(){
  var sparat = localStorage.getItem("onskelista-v3");
  if(!sparat){ uppdateraRaknare(); return }
  try{
    var arr = JSON.parse(sparat);
    for(var i=0; i<arr.length; i++){
      var p = hittaProdukt(arr[i].id);
      if(!p){ continue }
      var v = hittaVariant(p, arr[i].kod);
      if(!v){ continue }
      // bygg utan att spara om (vi ar mitt i ladd)
      laggTillUtanSpara(p, v);
    }
  } catch(err){ console.log("kunde inte lasa onskelista", err) }
  uppdateraRaknare();
}

function laggTillUtanSpara(p, v){
  var k = document.createElement("div");
  k.className = "onske-kort";
  k.setAttribute("role","listitem");
  k.setAttribute("tabindex","0");
  k.setAttribute("aria-label", p.namn + " " + v.farg);
  k.dataset.id = p.id;
  k.dataset.kod = v.kod;
  k.innerHTML =
    '<img src="' + v.bild + '" alt="' + p.namn + ' i ' + v.farg + '">' +
    '<span class="ta-bort">Ta bort</span>' +
    '<div class="info">' +
      '<span class="titel">' + p.namn + '</span>' +
      '<span class="pris-mini">' + v.farg + ' &middot; ' + p.pris + ' kr</span>' +
    '</div>';
  function taBort(){
    k.remove(); sparaOnskelista(); notis(p.namn + " togs bort");
  }
  k.addEventListener("click", taBort);
  k.addEventListener("keydown", function(e){
    if(e.key == "Enter" || e.key == " " || e.key == "Delete"){
      e.preventDefault(); taBort();
    }
  });
  var t = onskeYta.querySelector(".tom-text");
  if(t){ t.remove() }
  onskeYta.appendChild(k);
}

function hittaProdukt(id){
  for(var i=0; i<produkter.length; i++){ if(produkter[i].id == id){ return produkter[i] } }
  return null;
}
function hittaVariant(p, kod){
  for(var i=0; i<p.varianter.length; i++){ if(p.varianter[i].kod == kod){ return p.varianter[i] } }
  return null;
}

if(rensaRutorBtn){
  rensaRutorBtn.addEventListener("click", function(){
    var alla = onskeYta.querySelectorAll(".onske-kort");
    for(var i=0; i<alla.length; i++){ alla[i].remove() }
    localStorage.removeItem("onskelista-v3");
    uppdateraRaknare();
    notis("Onskelistan tomdes");
  });
}

laddaOnskelista();


// ============ VADER (Fetch nr 1) - rekommendera produkt ============
var hamtaVader = document.getElementById("hamta-vader");
var vaderYta = document.getElementById("vader-yta");

function jackTipsProdukt(t){
  // returnerar produkt-id + emoji + text
  if(t < 0)  return { i:"❄️", id:"8805",  text:"Storm Puffer - vadderad och vindtat for iskalla dagar." };
  if(t < 8)  return { i:"🧥", id:"F0445", text:"Inci Coat - vattentat och vindtat. Var bestseller." };
  if(t < 15) return { i:"🍂", id:"F0473", text:"Aurora Coat - oversize-snitt for hostvader." };
  if(t < 22) return { i:"☁️", id:"F0474", text:"Forest Bomber - lattare passform for milda dagar." };
  return            { i:"☀️", id:"L01",   text:"Nordic Light - lattvikt for varma dagar." };
}

if(hamtaVader){
  hamtaVader.addEventListener("click", function(){
    vaderYta.innerHTML = "Hamtar vader for Stockholm...";
    fetch("https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.07&current=temperature_2m,wind_speed_10m")
      .then(function(svar){
        if(!svar.ok){ throw new Error("api fel") }
        return svar.json();
      })
      .then(function(data){
        var t = data.current.temperature_2m;
        var v = data.current.wind_speed_10m;
        var tip = jackTipsProdukt(t);
        var produkt = hittaProdukt(tip.id);
        var bild = produkt ? produkt.varianter[0].bild : "";
        vaderYta.innerHTML =
          '<span class="stor">' + tip.i + '</span>' +
          '<div class="text">' +
            '<strong>' + t + '°C</strong> i Stockholm, vind ' + v + ' m/s.' +
            '<span class="tip">Vi rekommenderar: ' + tip.text + '</span>' +
          '</div>' +
          (bild ? '<img class="vader-bild" src="' + bild + '" alt="' + (produkt ? produkt.namn : "Rekommenderad jacka") + '">' : '');
      })
      .catch(function(err){
        vaderYta.textContent = "Kunde inte hamta vader just nu.";
        console.log(err);
      });
  });
}


// ============ FAKTA (Fetch nr 2) ============
var hamtaFakta = document.getElementById("hamta-fakta");
var faktaText = document.getElementById("fakta-text");
if(hamtaFakta){
  hamtaFakta.addEventListener("click", function(){
    faktaText.textContent = "Hamtar...";
    fetch("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
      .then(function(s){ if(!s.ok){ throw new Error("api fel") } return s.json() })
      .then(function(data){ faktaText.textContent = "Visste du: " + data.text })
      .catch(function(err){
        faktaText.textContent = "Kunde inte hamta tips just nu. Forsok igen.";
        console.log(err);
      });
  });
}
