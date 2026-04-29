// Mohammad Sami Alsharef
// gemensam js for hela webbplatsen. tema-knapp + canvas-rektangel

// ---- tema toggle (mork / ljus) ----
function vaxlaTema() {
  document.body.classList.toggle("dark");
  // sparar valet sa det halls kvar nar man byter sida
  if (document.body.classList.contains("dark")) {
    localStorage.setItem("tema", "dark");
  } else {
    localStorage.setItem("tema", "ljus");
  }
}

// ladda tidigare val nar sidan oppnas
window.addEventListener("DOMContentLoaded", function() {
  var sparat = localStorage.getItem("tema");
  if (sparat === "dark") {
    document.body.classList.add("dark");
  }

  // koppla knappen om den finns pa sidan
  var knapp = document.getElementById("tema-knapp");
  if (knapp) {
    knapp.addEventListener("click", vaxlaTema);
  }

  // om sidan har en canvas, rita rektangel
  var c = document.getElementById("minCanvas");
  if (c) {
    var ctx = c.getContext("2d");
    ctx.fillStyle = "#1f3a5f";
    ctx.fillRect(40, 30, 220, 120);

    // text ovanpa
    ctx.fillStyle = "#c8a96e";
    ctx.font = "bold 20px Arial";
    ctx.fillText("Hej fran canvas!", 60, 95);
  }
});
