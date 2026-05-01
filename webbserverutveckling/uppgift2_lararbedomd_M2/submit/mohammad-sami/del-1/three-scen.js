// Three.js scen for Samis Jackets - en produkt-display
// Tanken: jackan ligger pa en sockel pa ett podium, kameran kretsar runt
// (som de roterande produkt-vyerna pa Apple sin webshop).
// Belysning: ett mjukt vitt huvudljus + en sage-gron rim-light
// for att lyfta fram brand-fargen #c3cca6.

var box = document.getElementById("three-box");
var bredd = box.clientWidth;
var hojd = 480;

// ----- scen + kamera + renderer -----
var scen = new THREE.Scene();
scen.background = new THREE.Color(0xf9f9f9);

var kamera = new THREE.PerspectiveCamera(45, bredd / hojd, 0.1, 100);
kamera.position.set(0, 1.4, 5);
kamera.lookAt(0, 0.6, 0);

var renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(bredd, hojd);
renderer.setPixelRatio(window.devicePixelRatio);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
box.appendChild(renderer.domElement);


// ----- belysning -----
// mjukt fyll-ljus sa inget blir helt svart
var ambient = new THREE.AmbientLight(0xffffff, 0.55);
scen.add(ambient);

// huvudljus uppifran (key light)
var keyLight = new THREE.DirectionalLight(0xffffff, 0.9);
keyLight.position.set(3, 5, 4);
keyLight.castShadow = true;
keyLight.shadow.mapSize.width = 1024;
keyLight.shadow.mapSize.height = 1024;
scen.add(keyLight);

// sage rim-light fran sidan - ger brand-glow
var rimLight = new THREE.DirectionalLight(0xc3cca6, 0.6);
rimLight.position.set(-4, 2, -2);
scen.add(rimLight);


// ----- golv (podium) -----
var golvGeo = new THREE.CircleGeometry(2.5, 64);
var golvMat = new THREE.MeshStandardMaterial({
  color: 0xeaeaea,
  roughness: 0.4,
  metalness: 0.1
});
var golv = new THREE.Mesh(golvGeo, golvMat);
golv.rotation.x = -Math.PI / 2;
golv.receiveShadow = true;
scen.add(golv);


// ----- sockel under jackan -----
var sockelGeo = new THREE.CylinderGeometry(0.7, 0.9, 0.25, 48);
var sockelMat = new THREE.MeshStandardMaterial({
  color: 0xffffff,
  roughness: 0.3,
  metalness: 0.2
});
var sockel = new THREE.Mesh(sockelGeo, sockelMat);
sockel.position.y = 0.125;
sockel.castShadow = true;
sockel.receiveShadow = true;
scen.add(sockel);


// ----- "jackan" - en grupp med torso + krage + armar -----
// (forenklad geometri - en riktig modell skulle krava en .glb fil)
var jacka = new THREE.Group();

// torso = en utdragen box med rundade kanter (bara box, men sage-gron)
var torsoGeo = new THREE.BoxGeometry(1.0, 1.3, 0.5);
var torsoMat = new THREE.MeshStandardMaterial({
  color: 0xc3cca6,
  roughness: 0.7,
  metalness: 0.05
});
var torso = new THREE.Mesh(torsoGeo, torsoMat);
torso.position.y = 0.95;
torso.castShadow = true;
jacka.add(torso);

// krage = mindre cylinder pa toppen
var krageGeo = new THREE.CylinderGeometry(0.28, 0.32, 0.25, 24);
var krageMat = new THREE.MeshStandardMaterial({
  color: 0x000000,
  roughness: 0.5
});
var krage = new THREE.Mesh(krageGeo, krageMat);
krage.position.y = 1.7;
krage.castShadow = true;
jacka.add(krage);

// vanster arm
var armGeo = new THREE.CylinderGeometry(0.18, 0.16, 1.2, 16);
var armMat = new THREE.MeshStandardMaterial({
  color: 0xc3cca6,
  roughness: 0.7
});
var armV = new THREE.Mesh(armGeo, armMat);
armV.position.set(-0.65, 0.95, 0);
armV.rotation.z = 0.25;
armV.castShadow = true;
jacka.add(armV);

// hoger arm
var armH = new THREE.Mesh(armGeo, armMat);
armH.position.set(0.65, 0.95, 0);
armH.rotation.z = -0.25;
armH.castShadow = true;
jacka.add(armH);

// brand-knapp - en liten guldfargad sfar pa brostet
var knappGeo = new THREE.SphereGeometry(0.06, 16, 16);
var knappMat = new THREE.MeshStandardMaterial({
  color: 0x82a31a,
  metalness: 0.6,
  roughness: 0.2
});
var knapp = new THREE.Mesh(knappGeo, knappMat);
knapp.position.set(0, 1.0, 0.27);
jacka.add(knapp);

scen.add(jacka);


// ----- animations-loop: kamera kretsar runt -----
var vinkel = 0;
function loop() {
  requestAnimationFrame(loop);

  vinkel += 0.005;
  kamera.position.x = Math.sin(vinkel) * 4.2;
  kamera.position.z = Math.cos(vinkel) * 4.2;
  kamera.position.y = 1.6 + Math.sin(vinkel * 0.5) * 0.2;
  kamera.lookAt(0, 1.0, 0);

  // jackan svajar lite for liv
  jacka.rotation.y = Math.sin(vinkel * 0.7) * 0.1;

  renderer.render(scen, kamera);
}
loop();


// ----- responsivt: anpassa nar fonstret andras -----
window.addEventListener("resize", function() {
  var nyBredd = box.clientWidth;
  kamera.aspect = nyBredd / hojd;
  kamera.updateProjectionMatrix();
  renderer.setSize(nyBredd, hojd);
});
