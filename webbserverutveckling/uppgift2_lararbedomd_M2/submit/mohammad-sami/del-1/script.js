// Mohammad Sami Alsharef
// gemensam js for hela mediagalleriet
// tema-knapp + canvas. Samma stil som forra uppgiften (var, ==).

// ----- TEMA-KNAPP -----
// default ar LJUST (precis som i appen). Knappen byter till morkt.
var temaBtn = document.getElementById("tema-btn");
var morkt = false;

// kollar om man redan valt morkt forra gangen
if (localStorage.getItem("tema") == "morkt") {
  document.body.classList.add("morkt");
  morkt = true;
}

if (temaBtn) {
  // visar ratt text vid sidladdning
  if (morkt == true) {
    temaBtn.textContent = "Ljust";
  } else {
    temaBtn.textContent = "Morkt";
  }

  temaBtn.addEventListener("click", function() {
    morkt = !morkt;
    if (morkt == true) {
      document.body.classList.add("morkt");
      temaBtn.textContent = "Ljust";
      localStorage.setItem("tema", "morkt");
    } else {
      document.body.classList.remove("morkt");
      temaBtn.textContent = "Morkt";
      localStorage.setItem("tema", "ljust");
    }
  });
}


// ----- CANVAS - rita en G&S logga -----
// markesfargerna fran appen: sage #c3cca6, olive #82a31a, svart text.
var c = document.getElementById("minCanvas");
if (c) {
  var ctx = c.getContext("2d");

  // ljust kort i bakgrunden
  ctx.fillStyle = "#f9f9f9";
  ctx.fillRect(0, 0, 360, 200);

  // sage stripe - markesaccenten
  ctx.fillStyle = "#c3cca6";
  ctx.fillRect(0, 60, 360, 80);

  // svart kontur runt ramen
  ctx.strokeStyle = "#000000";
  ctx.lineWidth = 2;
  ctx.strokeRect(20, 20, 320, 160);

  // huvudtexten - serif kanns mer som appen
  ctx.fillStyle = "#000000";
  ctx.font = "bold 38px Georgia";
  ctx.fillText("G&S", 140, 110);

  // undertexten i olive
  ctx.fillStyle = "#82a31a";
  ctx.font = "13px Helvetica";
  ctx.fillText("S A M I S   J A C K E T S", 90, 145);
}
