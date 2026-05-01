// script.js - M3 Sami
// DOM + Fetch + LocalStorage + tema

// ---- tema knapen ---------------------------------------
var temaBtn = document.getElementById("tema-btn");
var morkt = false;

if(localStorage.getItem("tema") == "morkt"){
  document.body.classList.add("morkt");
  morkt = true;
}

if(temaBtn){
  if(morkt){ temaBtn.textContent = "Ljust"; temaBtn.setAttribute("aria-pressed","true") }
  temaBtn.addEventListener("click", function(){
    morkt = !morkt;
    if(morkt){
      document.body.classList.add("morkt");
      temaBtn.textContent = "Ljust";
      temaBtn.setAttribute("aria-pressed","true");
      localStorage.setItem("tema","morkt");
    } else {
      document.body.classList.remove("morkt");
      temaBtn.textContent = "Morkt";
      temaBtn.setAttribute("aria-pressed","false");
      localStorage.setItem("tema","ljust");
    }
  });
}


// ---- 1. namn med localStorage --------------------------
var form = document.getElementById("namn-form");
var input = document.getElementById("namn-input");
var hellsning = document.getElementById("hellsning");
var rensaNamn = document.getElementById("rensa-namn");

// visa sparat namn direkt nar sidan oppnas
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
  });
}

if(rensaNamn){
  rensaNamn.addEventListener("click", function(){
    localStorage.removeItem("kund-namn");
    input.value = "";
    hellsning.textContent = "(namn rensat)";
  });
}


// ---- 2. DOM - skapa rutor (onskelista) -----------------
var skapaBtn = document.getElementById("skapa");
var rensaRutorBtn = document.getElementById("rensa-rutor");
var yta = document.getElementById("rutor-yta");

// markesfarger fran appen
var fargBank = ["#c3cca6","#82a31a","#e8d3a3","#d4b3e8","#a3c4e8","#e8a3a3","#a3e8c4"];

// jacka modeller (slumpas)
var jackor = ["Inci Coat","Storm Parka","Aurora Down","Forest Bomber","Edda Trench","Nordic Puffer"];

// laddar sparade rutor fran localStorage
function laddaRutor(){
  var sparat = localStorage.getItem("onskelista");
  if(sparat){
    try{
      var arr = JSON.parse(sparat);
      for(var i=0; i<arr.length; i++){
        ritaRuta(arr[i].namn, arr[i].farg, false);
      }
    } catch(err){ console.log("kunde inte lasa onskelista") }
  }
}

function sparaRutor(){
  var alla = yta.querySelectorAll(".rutan");
  var arr = [];
  for(var i=0; i<alla.length; i++){
    arr.push({ namn: alla[i].textContent, farg: alla[i].style.backgroundColor });
  }
  localStorage.setItem("onskelista", JSON.stringify(arr));
}

function ritaRuta(namn, farg, sparaOcksa){
  var d = document.createElement("div");
  d.className = "rutan";
  d.textContent = namn;
  d.style.backgroundColor = farg;
  d.setAttribute("role","listitem");
  d.setAttribute("tabindex","0");
  d.setAttribute("aria-label", namn + " - klicka for att ta bort");
  // klicka for att ta bort
  d.addEventListener("click", function(){
    d.remove();
    sparaRutor();
  });
  // tangentbord - Enter eller Delete
  d.addEventListener("keydown", function(e){
    if(e.key == "Enter" || e.key == "Delete"){
      d.remove();
      sparaRutor();
    }
  });
  yta.appendChild(d);
  if(sparaOcksa){ sparaRutor() }
}

if(skapaBtn){
  skapaBtn.addEventListener("click", function(){
    var n = jackor[Math.floor(Math.random() * jackor.length)];
    var f = fargBank[Math.floor(Math.random() * fargBank.length)];
    ritaRuta(n, f, true);
  });
}

if(rensaRutorBtn){
  rensaRutorBtn.addEventListener("click", function(){
    yta.innerHTML = "";
    localStorage.removeItem("onskelista");
  });
}

laddaRutor();


// ---- 3. Fetch API - hamtar tips -------------------------
var hamtaBtn = document.getElementById("hamta-fakta");
var faktaText = document.getElementById("fakta-text");

if(hamtaBtn){
  hamtaBtn.addEventListener("click", function(){
    faktaText.textContent = "Hamtar...";
    fetch("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
      .then(function(svar){
        if(!svar.ok){ throw new Error("api fel") }
        return svar.json();
      })
      .then(function(data){
        // kort "modetips"-twist
        faktaText.textContent = "Visste du: " + data.text;
      })
      .catch(function(err){
        faktaText.textContent = "Kunde inte hamta tips just nu. Forsok igen.";
        console.log(err);
      });
  });
}
