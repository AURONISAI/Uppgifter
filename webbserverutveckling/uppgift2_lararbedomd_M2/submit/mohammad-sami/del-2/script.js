// script.js - del 2 (fixad)

// FIX: dopte om "test" till nat begripligt
function visaTal(){
  // FIX: var -> const, lade till semikolon
  const x = 10;
  console.log(x);
}  // FIX: stangande } saknades i originalet -> SyntaxError

// FIX: funktionen kallades aldrig, gor det nu
window.addEventListener("DOMContentLoaded", function(){
  visaTal();
});
