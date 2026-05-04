// script.js
// Sami - M3

// mina jackor
var jackor = [
  { id:"8805",  namn:"Storm Puffer",   pris:2999, beskr:"Vadderad puffer-jacka. Vindtat och varm." },
  { id:"F0357", namn:"Edda Long",      pris:3499, beskr:"Lang trenchcoat, tidlos." },
  { id:"F0445", namn:"Inci Coat",      pris:2499, beskr:"Var bestseller. Vattentat." },
  { id:"F0473", namn:"Aurora Coat",    pris:2799, beskr:"Modern oversize." },
  { id:"F0474", namn:"Forest Bomber",  pris:1899, beskr:"Bomberjacka." },
  { id:"L01",   namn:"Nordic Light",   pris:1599, beskr:"Lattvikt-jacka." }
];

// farger per jacka. Detta blev lite langt men jag visste inte hur jag skulle gora annars
var farger = {
  "8805": [
    { kod:"beige",       namn:"Beige",         hex:"#d8c8a8", bild:"assets/produkter/8805_beige.jpg" },
    { kod:"beige_black", namn:"Beige & Svart", hex:"#3a3a3a", bild:"assets/produkter/8805_beige_black.jpg" },
    { kod:"black",       namn:"Svart",         hex:"#111",    bild:"assets/produkter/8805_black.jpg" }
  ],
  "F0357": [
    { kod:"black",       namn:"Svart",        hex:"#111",    bild:"assets/produkter/F0357_black.jpg" },
    { kod:"brown",       namn:"Brun",         hex:"#6b4423", bild:"assets/produkter/F0357_brown.jpg" },
    { kod:"brown_black", namn:"Brun & Svart", hex:"#3a2a18", bild:"assets/produkter/F0357_brown_black.jpg" }
  ],
  "F0445": [
    { kod:"beige",       namn:"Beige",         hex:"#d8c8a8", bild:"assets/produkter/F0445_beige.jpg" },
    { kod:"beige_brown", namn:"Beige & Brun",  hex:"#a07a4a", bild:"assets/produkter/F0445_beige_brown.jpg" },
    { kod:"black",       namn:"Svart",         hex:"#111",    bild:"assets/produkter/F0445_black.jpg" },
    { kod:"black_beige", namn:"Svart & Beige", hex:"#3a3a3a", bild:"assets/produkter/F0445_black_beige.jpg" },
    { kod:"brown",       namn:"Brun",          hex:"#6b4423", bild:"assets/produkter/F0445_brown.jpg" }
  ],
  "F0473": [
    { kod:"beige",       namn:"Beige",         hex:"#d8c8a8", bild:"assets/produkter/F0473_beige.jpg" },
    { kod:"beige_brown", namn:"Beige & Brun",  hex:"#a07a4a", bild:"assets/produkter/F0473_beige_brown.jpg" },
    { kod:"black",       namn:"Svart",         hex:"#111",    bild:"assets/produkter/F0473_black.jpg" },
    { kod:"black_beige", namn:"Svart & Beige", hex:"#3a3a3a", bild:"assets/produkter/F0473_black_beige.jpg" },
    { kod:"brown",       namn:"Brun",          hex:"#6b4423", bild:"assets/produkter/F0473_brown.jpg" }
  ],
  "F0474": [
    { kod:"beige",       namn:"Beige",         hex:"#d8c8a8", bild:"assets/produkter/F0474_beige.jpg" },
    { kod:"beige_khaki", namn:"Beige & Khaki", hex:"#7a8458", bild:"assets/produkter/F0474_beige_khaki.jpg" },
    { kod:"khaki",       namn:"Khaki",         hex:"#5a6438", bild:"assets/produkter/F0474_khaki.jpg" }
  ],
  "L01": [
    { kod:"black", namn:"Svart", hex:"#111",    bild:"assets/produkter/L01_black.jpg" },
    { kod:"green", namn:"Gron",  hex:"#3e6b3a", bild:"assets/produkter/L01_green.jpg" }
  ]
};


// hamtar saker fran sidan
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



// rita kataloge
function ritaKatalog(){

  // gor en kopia sa jag inte forstor min jackor-array
  var lista = [];
  for(var i=0; i<jackor.length; i++){
    lista.push(jackor[i]);
  }

  // filter pa farg
  if(filter.value != "alla"){
    var nyLista = [];
    for(var i=0; i<lista.length; i++){
      var jackaFarger = farger[lista[i].id];
      var hittade = false;
      for(var j=0; j<jackaFarger.length; j++){
        // anvander indexOf for att kolla om kod innehaller filtret
        if(jackaFarger[j].kod.indexOf(filter.value) > -1){
          hittade = true;
        }
      }
      if(hittade == true){
        nyLista.push(lista[i]);
      }
    }
    lista = nyLista;
  }

  // sortera
  if(sort.value == "pris-upp"){
    lista.sort(function(a, b){ return a.pris - b.pris });
  }
  if(sort.value == "pris-ner"){
    lista.sort(function(a, b){ return b.pris - a.pris });
  }
  if(sort.value == "namn"){
    lista.sort(function(a, b){
      if(a.namn < b.namn){ return -1 }
      if(a.namn > b.namn){ return 1 }
      return 0;
    });
  }

  // tom ut och rita igen
  katalog.innerHTML = "";
  for(var i=0; i<lista.length; i++){
    var p = lista[i];
    var v = farger[p.id][0]; // forsta fargen som huvudbild

    // bygg cirklar for fargerna
    var cirklar = "";
    for(var k=0; k<farger[p.id].length; k++){
      cirklar = cirklar + '<span class="cirkel" style="background:' + farger[p.id][k].hex + '"></span>';
    }

    var html = '';
    html = html + '<div class="kort" tabindex="0" role="listitem" data-id="' + p.id + '">';
    html = html + '  <div class="bild"><img src="' + v.bild + '" alt="' + p.namn + '"></div>';
    html = html + '  <div class="info">';
    html = html + '    <span class="titel">' + p.namn + '</span>';
    html = html + '    <span class="sku">art. ' + p.id + '</span>';
    html = html + '    <span class="pris">' + p.pris + ' kr</span>';
    html = html + '    <div class="farger">' + cirklar + '</div>';
    html = html + '  </div>';
    html = html + '</div>';

    katalog.innerHTML = katalog.innerHTML + html;
  }

  antalText.textContent = lista.length + " av " + jackor.length;

  // jag fick lagga eventet HAR for att korten ar nybyggda varje gang
  // funkade inte forst nar jag hade det utanfor
  var allaKort = document.querySelectorAll(".kort");
  for(var i=0; i<allaKort.length; i++){
    allaKort[i].onclick = function(){
      var id = this.getAttribute("data-id");
      oppna(id);
    };
    allaKort[i].onkeydown = function(e){
      if(e.key == "Enter"){
        var id = this.getAttribute("data-id");
        oppna(id);
      }
    };
  }
}


// hitta en jacka pa id
function hittaJacka(id){
  for(var i=0; i<jackor.length; i++){
    if(jackor[i].id == id){
      return jackor[i];
    }
  }
  return null;
}


// MODAL
var aktivJacka = null;
var aktivFarg = null;

function oppna(id){
  aktivJacka = hittaJacka(id);
  aktivFarg = farger[id][0];
  visaModal();

  // bygg fargknappar
  mFargvalj.innerHTML = "";
  for(var i=0; i<farger[id].length; i++){
    var f = farger[id][i];
    var b = document.createElement("button");
    b.className = "farg-knapp";
    if(f == aktivFarg){
      b.className = "farg-knapp vald";
    }
    b.style.background = f.hex;
    b.title = f.namn;
    b.setAttribute("type", "button");
    b.setAttribute("data-kod", f.kod);
    b.onclick = bytFarg;
    mFargvalj.appendChild(b);
  }

  modal.classList.add("oppen");
  modal.setAttribute("aria-hidden", "false");
}

function bytFarg(){
  var kod = this.getAttribute("data-kod");
  // hitta ratt farg-objekt
  var lista = farger[aktivJacka.id];
  for(var i=0; i<lista.length; i++){
    if(lista[i].kod == kod){
      aktivFarg = lista[i];
    }
  }
  // ta bort vald-klass fran alla
  var alla = document.querySelectorAll(".farg-knapp");
  for(var i=0; i<alla.length; i++){
    alla[i].classList.remove("vald");
  }
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

modal.onclick = function(e){
  // bara om man klickar pa svarta bakgrunden, inte pa innehallet
  if(e.target == modal){
    stang();
  }
};

document.onkeydown = function(e){
  if(e.key == "Escape"){
    stang();
  }
};


// LAGG TILL i onske
document.getElementById("modal-lagg-till").onclick = function(){
  if(aktivJacka == null){ return }
  laggTill(aktivJacka, aktivFarg);
  stang();
};

function laggTill(p, f){
  // ta bort tom-text om den finns
  var tom = onskeYta.querySelector(".tom-text");
  if(tom != null){
    tom.remove();
  }

  var k = document.createElement("div");
  k.className = "onske-kort";
  k.setAttribute("tabindex", "0");
  k.setAttribute("data-id", p.id);
  k.setAttribute("data-kod", f.kod);
  k.innerHTML =
    '<img src="' + f.bild + '" alt="' + p.namn + '">' +
    '<div class="info">' +
      '<span class="titel">' + p.namn + '</span>' +
      '<span class="pris-mini">' + f.namn + ' - ' + p.pris + ' kr</span>' +
    '</div>';

  k.onclick = function(){
    k.remove();
    spara();
    visaToast(p.namn + " togs bort");
  };
  k.onkeydown = function(e){
    if(e.key == "Enter" || e.key == "Delete"){
      k.remove();
      spara();
      visaToast(p.namn + " togs bort");
    }
  };

  onskeYta.appendChild(k);
  spara();
  visaToast(p.namn + " tillagd");
}


// spara/ladda fran localStorage
function spara(){
  var alla = document.querySelectorAll(".onske-kort");
  var arr = [];
  for(var i=0; i<alla.length; i++){
    arr.push({
      id: alla[i].getAttribute("data-id"),
      kod: alla[i].getAttribute("data-kod")
    });
  }
  localStorage.setItem("onskelista", JSON.stringify(arr));
  uppdateraRaknare();
}

function ladda(){
  var data = localStorage.getItem("onskelista");
  if(data == null){
    uppdateraRaknare();
    return;
  }
  var arr = JSON.parse(data);
  for(var i=0; i<arr.length; i++){
    var p = hittaJacka(arr[i].id);
    if(p == null){ continue }
    // hitta fargen
    var f = null;
    var fl = farger[arr[i].id];
    for(var j=0; j<fl.length; j++){
      if(fl[j].kod == arr[i].kod){
        f = fl[j];
      }
    }
    if(f == null){ continue }
    laggTill(p, f);
  }
}

function uppdateraRaknare(){
  var n = document.querySelectorAll(".onske-kort").length;
  raknare.textContent = n + " jackor";
  varukorg.textContent = n + " i listan";

  if(n == 0 && onskeYta.querySelector(".tom-text") == null){
    var tom = document.createElement("p");
    tom.className = "tom-text";
    tom.textContent = "Tom. Lagg till en jacka fran katalogen.";
    onskeYta.appendChild(tom);
  }
}

document.getElementById("rensa-rutor").onclick = function(){
  var alla = document.querySelectorAll(".onske-kort");
  for(var i=0; i<alla.length; i++){
    alla[i].remove();
  }
  localStorage.removeItem("onskelista");
  uppdateraRaknare();
  visaToast("Onskelistan tomdes");
};


// toast
var toastTimer = null;
function visaToast(text){
  toast.textContent = text;
  toast.classList.add("visa");
  if(toastTimer != null){
    clearTimeout(toastTimer);
  }
  toastTimer = setTimeout(function(){
    toast.classList.remove("visa");
  }, 2000);
}


// TEMA
var temaBtn = document.getElementById("tema-btn");
if(localStorage.getItem("tema") == "morkt"){
  document.body.classList.add("morkt");
  temaBtn.setAttribute("aria-pressed", "true");
}
temaBtn.onclick = function(){
  document.body.classList.toggle("morkt");
  if(document.body.classList.contains("morkt")){
    localStorage.setItem("tema", "morkt");
    temaBtn.setAttribute("aria-pressed", "true");
  } else {
    localStorage.setItem("tema", "ljust");
    temaBtn.setAttribute("aria-pressed", "false");
  }
};


// FARG-pickern
var fargPick = document.getElementById("farg-pick");

function satFarg(hex){
  document.documentElement.style.setProperty("--accent", hex);
  // mjuk farg = samma hex med transparens
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


// VADER (fetch nr 1)
document.getElementById("hamta-vader").onclick = function(){
  var yta = document.getElementById("vader-yta");
  yta.textContent = "Hamtar...";

  fetch("https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.07&current=temperature_2m,wind_speed_10m")
    .then(function(svar){
      return svar.json();
    })
    .then(function(data){
      var temp = data.current.temperature_2m;
      var vind = data.current.wind_speed_10m;

      // valj jacka beroende pa temp
      var tipsId = "L01";
      var tipsText = "Nordic Light - lattvikt for varma dagar";

      if(temp < 0){
        tipsId = "8805";
        tipsText = "Storm Puffer - vadderad och vindtat";
      } else if(temp < 8){
        tipsId = "F0445";
        tipsText = "Inci Coat - vattentat och varm";
      } else if(temp < 15){
        tipsId = "F0473";
        tipsText = "Aurora Coat - oversize for hostvader";
      } else if(temp < 22){
        tipsId = "F0474";
        tipsText = "Forest Bomber - lattare for milda dagar";
      }

      var bild = farger[tipsId][0].bild;

      yta.innerHTML =
        '<div><strong>' + temp + '°C</strong> i Stockholm, vind ' + vind + ' m/s.<br>' +
        'Tips: ' + tipsText + '</div>' +
        '<img src="' + bild + '" alt="Tips">';
    })
    .catch(function(){
      yta.textContent = "Kunde inte hamta vader.";
    });
};


// FAKTA (fetch nr 2)
document.getElementById("hamta-fakta").onclick = function(){
  var p = document.getElementById("fakta-text");
  p.textContent = "Hamtar...";

  fetch("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    .then(function(svar){
      return svar.json();
    })
    .then(function(data){
      p.textContent = "Visste du: " + data.text;
    })
    .catch(function(){
      p.textContent = "Kunde inte hamta tips.";
    });
};


// kor!
filter.onchange = ritaKatalog;
sort.onchange = ritaKatalog;
ritaKatalog();
ladda();
