// script.js  - Sami
// tema knapen + canvas

var btn = document.getElementById("tema-btn");
var morkt = false;

// kollare om temat finns sparat
if(localStorage.getItem("tema") == "morkt"){
  document.body.classList.add("morkt");
  morkt = true;
}

if(btn){
  if(morkt == true){ btn.textContent = "Ljust" }
  else{ btn.textContent = "Morkt" }

  btn.addEventListener("click", function(){
    morkt = !morkt
    if(morkt){
      document.body.classList.add("morkt")
      btn.textContent = "Ljust"
      localStorage.setItem("tema","morkt")
    } else {
      document.body.classList.remove("morkt")
      btn.textContent = "Morkt"
      localStorage.setItem("tema","ljust")
    }
  });
}


// canvas - rita G&S loggan
var c = document.getElementById("minCanvas");
if(c){
  var ctx = c.getContext("2d");

  ctx.fillStyle = "#f9f9f9";
  ctx.fillRect(0,0,360,200);

  // sage stripe
  ctx.fillStyle = "#c3cca6";
  ctx.fillRect(0,60,360,80);

  // svart ram
  ctx.strokeStyle = "#000";
  ctx.lineWidth = 2;
  ctx.strokeRect(20,20,320,160);

  // text
  ctx.fillStyle = "#000";
  ctx.font = "bold 36px Georgia";
  ctx.fillText("G&S", 140, 110);

  ctx.fillStyle = "#82a31a";
  ctx.font = "13px Arial";
  ctx.fillText("SAMIS JACKETS", 115, 145);
}
