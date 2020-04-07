var sacha = {
  nombre :'sacha',
  edad:17,
  ingeniero: true,
  cocinero: false,
  cantante: false,
  dj: true,
  guitarra: false,
  drone: true
}

function imprimirprofesion (persona){
  console.log(`${persona.nombre} es :`)
  if (persona.edad>=18){
  console.log('es mayor');
}else {
  console.log('es menor');
}

}
imprimirprofesion(sacha)
