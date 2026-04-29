// roterande kub med en bildtextur
// koden ar ihopplockad fran exempel pa threejs.org sin docs

var scene = new THREE.Scene();
scene.background = new THREE.Color(0xeeeeee);

var camera = new THREE.PerspectiveCamera(70, window.innerWidth / 400, 0.1, 1000);
camera.position.z = 3;

var renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth * 0.9, 400);
document.getElementById("three-box").appendChild(renderer.domElement);

// textur fran en bild
var loader = new THREE.TextureLoader();
var textur = loader.load("https://threejs.org/examples/textures/crate.gif");

var geometri = new THREE.BoxGeometry(1.5, 1.5, 1.5);
var material = new THREE.MeshBasicMaterial({ map: textur });
var kub = new THREE.Mesh(geometri, material);
scene.add(kub);

function loop() {
  requestAnimationFrame(loop);
  kub.rotation.x += 0.01;
  kub.rotation.y += 0.012;
  renderer.render(scene, camera);
}
loop();
