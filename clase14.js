var sacha = {
  nombre : 'sacha',
  peso: 68,
  edad: 75,
  apellido: 'deded'
}

console.log(`al inicio del año ${sacha.nombre} pesa ${sacha.peso}`);
const INCREMENTO = 0.3
const AÑO = 365
var dias = 0
function aumentodepeso (persona) {
  return persona.peso += 200
}

const adelgazar = persona => persona.peso -= 200
const comeMucho = () => Math.random () < 0.3
const deporte = () => Math.random () < 0.4
const META = sacha.peso-3

while (sacha.peso > META) {
  if (comeMucho()){
    aumentodepeso (sacha)
  }else {
    adelgazar(sacha)
  }
  dias += 1
}

console.log(`pasaron ${dias} hasta q ${sacha.nombre}adelgazo`);
