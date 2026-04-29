// Mohammad Sami Alsharef
// gemensam js. tema-knapp + canvas. samma stil som GS appen sidan (var, ==).

// tema knapp - byter dark/light. dark ar default.
var temaBtn = document.getElementById("tema-btn");
var isLight = false;

// kollar om man redan valt light forra gangen
if (localStorage.getItem("tema") == "light") {
  document.body.classList.add("light");
  isLight = true;
}

if (temaBtn) {
  temaBtn.addEventListener("click", function() {
    isLight = !isLight;
    if (isLight == true) {
      document.body.classList.add("light");
      temaBtn.textContent = "Mork";
      localStorage.setItem("tema", "light");
    } else {
      document.body.classList.remove("light");
      temaBtn.textContent = "Tema";
      localStorage.setItem("tema", "dark");
    }
  });
}

// om sidan har en canvas, rita en jacka-skylt
var c = document.getElementById("minCanvas");
if (c) {
  var ctx = c.getContext("2d");

  // gold ram
  ctx.fillStyle = "#c8a96e";
  ctx.fillRect(20, 20, 280, 140);

  // svart insida
  ctx.fillStyle = "#000";
  ctx.fillRect(28, 28, 264, 124);

  // text - GS logga
  ctx.fillStyle = "#c8a96e";
  ctx.font = "bold 28px Arial";
  ctx.fillText("G&S", 130, 80);

  ctx.font = "12px Arial";
  ctx.fillText("by Samis Jackets", 100, 110);
}
