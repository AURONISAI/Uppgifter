// FIX: gav funktionen ett battre namn an "test"
function visaTal() {
  // FIX: bytte var till const eftersom variabeln aldrig andras
  // FIX: la till semikolon i slutet av raderna (god vana, undviker fel)
  const x = 10;
  console.log(x);
} // FIX: hela funktionen saknade en stangande } i originalet - det gav syntax error och inget script korde alls

// FIX: funktionen anropades aldrig i originalet, sa inget hande.
// Nu kor jag den nar sidan ar laddad.
window.addEventListener("DOMContentLoaded", function() {
  visaTal();
});
