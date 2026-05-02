// script.js - M3 v2 - Sami
// Bygger pa M2-designen. DOM + Fetch + LocalStorage + tema + accentfarg + toast.

// ---- toast (notiser) ----
var toast = document.getElementById("toast");
var toastTimer;
function notis(text){
  if(!toast){ return }
  toast.textContent = text;
  toast.classList.add("visa");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(function(){ toast.classList.remove("visa") }, 2400);
}


// ---- tema knapp (samma logik som M2) ----
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


// ---- accentfarg ----
var fargPick = document.getElementById("farg-pick");
var aterstall = document.getElementById("aterstall-farg");

function satFarg(hex){
  document.documentElement.style.setProperty("--accent", hex);
  document.documentElement.style.setProperty("--accent-mjuk", hex + "55");
}

var sparadFarg = localStorage.getItem("accent");
if(sparadFarg){
  satFarg(sparadFarg);
  if(fargPick){ fargPick.value = sparadFarg }
}

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


// ---- 1. NAMN ----
var form = document.getElementById("namn-form");
var input = document.getElementById("namn-input");
var hellsning = document.getElementById("hellsning");
var rensaNamn = document.getElementById("rensa-namn");

var sparatNamn = localStorage.getItem("kund-namn");
if(sparatNamn){
  hellsning.textContent = "Valkommen tillbaka, " + sparatNamn + "!";
  input.value = sparatNamn;
}

if(form){
  form.addEventListener("submit", function(e){
    e.preventDefault();
    var n = input.value.trim();
    if(n == ""){ return }
    localStorage.setItem("kund-namn", n);
    hellsning.textContent = "Valkommen, " + n + "!";
    notis("Namn sparat");
  });
}

if(rensaNamn){
  rensaNamn.addEventListener("click", function(){
    localStorage.removeItem("kund-namn");
    input.value = "";
    hellsning.textContent = "(namn rensat)";
    notis("Namn rensat");
  });
}


// ---- 2. ONSKELISTA - riktiga produktkort med Unsplash-bilder ----
var skapaBtn = document.getElementById("skapa");
var rensaRutorBtn = document.getElementById("rensa-rutor");
var yta = document.getElementById("rutor-yta");
var raknare = document.getElementById("raknare");

// kollektion: namn, pris, bild (Unsplash)
var jackor = [
  { namn:"Inci Coat",
    pris:"2 499 kr",
    bild:"https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=600&q=70" },
  { namn:"Storm Parka",
    pris:"3 199 kr",
    bild:"https://images.unsplash.com/photo-1544022613-e87ca75a784a?w=600&q=70" },
  { namn:"Aurora Down",
    pris:"2 799 kr",
    bild:"https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600&q=70" },
  { namn:"Forest Bomber",
    pris:"1 899 kr",
    bild:"https://images.unsplash.com/photo-1542327897-d73f4005b533?w=600&q=70" },
  { namn:"Edda Trench",
    pris:"2 299 kr",
    bild:"https://images.unsplash.com/photo-1539533113208-f6df8cc8b543?w=600&q=70" },
  { namn:"Nordic Puffer",
    pris:"3 499 kr",
    bild:"https://images.unsplash.com/photo-1548883354-94bcfe321cbb?w=600&q=70" }
];

function uppdateraRaknare(){
  var n = yta.querySelectorAll(".kort").length;
  raknare.textContent = n + " jackor";
}

function ritaKort(j, sparaOcksa){
  var k = document.createElement("div");
  k.className = "kort";
  k.setAttribute("role","listitem");
  k.setAttribute("tabindex","0");
  k.setAttribute("aria-label", j.namn + " - " + j.pris + " - klicka eller tryck Enter for att ta bort");
  k.dataset.namn = j.namn;
  k.dataset.pris = j.pris;
  k.dataset.bild = j.bild;

  k.innerHTML =
    '<img src="' + j.bild + '" alt="Produktbild av ' + j.namn + '">' +
    '<span class="ta-bort">Ta bort</span>' +
    '<div class="info">' +
      '<span class="titel">' + j.namn + '</span>' +
      '<span class="pris">' + j.pris + '</span>' +
    '</div>';

  function taBort(){
    k.remove();
    sparaRutor();
    notis(j.namn + " togs bort");
  }

  k.addEventListener("click", taBort);
  k.addEventListener("keydown", function(e){
    if(e.key == "Enter" || e.key == " " || e.key == "Delete"){
      e.preventDefault();
      taBort();
    }
  });

  yta.appendChild(k);
  if(sparaOcksa){ sparaRutor() }
}

function sparaRutor(){
  var alla = yta.querySelectorAll(".kort");
  var arr = [];
  for(var i=0; i<alla.length; i++){
    arr.push({
      namn: alla[i].dataset.namn,
      pris: alla[i].dataset.pris,
      bild: alla[i].dataset.bild
    });
  }
  localStorage.setItem("onskelista", JSON.stringify(arr));
  uppdateraRaknare();
}

function laddaRutor(){
  var sparat = localStorage.getItem("onskelista");
  if(!sparat){ return }
  try{
    var arr = JSON.parse(sparat);
    for(var i=0; i<arr.length; i++){ ritaKort(arr[i], false) }
  } catch(err){ console.log("kunde inte lasa onskelista", err) }
  uppdateraRaknare();
}

if(skapaBtn){
  skapaBtn.addEventListener("click", function(){
    var j = jackor[Math.floor(Math.random() * jackor.length)];
    ritaKort(j, true);
    notis(j.namn + " tillagd i onskelistan");
  });
}

if(rensaRutorBtn){
  rensaRutorBtn.addEventListener("click", function(){
    yta.innerHTML = "";
    localStorage.removeItem("onskelista");
    uppdateraRaknare();
    notis("Onskelistan tomdes");
  });
}

laddaRutor();


// ---- 3. VADER (Fetch nr 1) ----
var hamtaVader = document.getElementById("hamta-vader");
var vaderYta = document.getElementById("vader-yta");

function jackTips(t){
  if(t < 0)  return { i:"❄️", t:"Storm Parka eller Aurora Down - det ar iskallt!" };
  if(t < 8)  return { i:"🧥", t:"Inci Coat passar - vattentat och varm." };
  if(t < 15) return { i:"🍂", t:"Forest Bomber for hostvader." };
  if(t < 22) return { i:"☁️", t:"Edda Trench - lagom for milda dagar." };
  return            { i:"☀️", t:"Ingen jacka behovs - njut av solen!" };
}

if(hamtaVader){
  hamtaVader.addEventListener("click", function(){
    vaderYta.textContent = "Hamtar vader for Stockholm...";
    fetch("https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.07&current=temperature_2m,wind_speed_10m")
      .then(function(svar){
        if(!svar.ok){ throw new Error("api fel") }
        return svar.json();
      })
      .then(function(data){
        var t = data.current.temperature_2m;
        var v = data.current.wind_speed_10m;
        var tip = jackTips(t);
        vaderYta.innerHTML =
          '<span class="stor">' + tip.i + '</span>' +
          '<strong>' + t + '°C</strong> i Stockholm, vind ' + v + ' m/s.' +
          '<span class="tip">' + tip.t + '</span>';
      })
      .catch(function(err){
        vaderYta.textContent = "Kunde inte hamta vader just nu.";
        console.log(err);
      });
  });
}


// ---- 4. FAKTA (Fetch nr 2) ----
var hamtaFakta = document.getElementById("hamta-fakta");
var faktaText = document.getElementById("fakta-text");

if(hamtaFakta){
  hamtaFakta.addEventListener("click", function(){
    faktaText.textContent = "Hamtar...";
    fetch("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
      .then(function(s){ if(!s.ok){ throw new Error("api fel") } return s.json() })
      .then(function(data){
        faktaText.textContent = "Visste du: " + data.text;
      })
      .catch(function(err){
        faktaText.textContent = "Kunde inte hamta tips just nu. Forsok igen.";
        console.log(err);
      });
  });
}
