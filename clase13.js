var sacha = {
  nombre : 'sacha',
  peso: 68,
  edad: 75,
  apellido: 'deded'
}

console.log(`al inicio del año ${sacha.nombre} pesa ${sacha.peso}`);

function aumentodepeso (persona) {
  return persona.peso += 200
}

const adelgazar = persona => persona.peso -= 200

for (var i = 1; i <= 365; i++) {
  var random = Math.random ()

  if(random < 0.25){
    aumentodepeso (sacha)
  }else {
    adelgazar (sacha)
  }

}


console.log(`al final del año ${sacha.nombre} pesa ${sacha.peso.toFixed(2)}`);
