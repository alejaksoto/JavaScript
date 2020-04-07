var sacha = {
  nombre :'sacha',
  apellido: 'jum',
  edad: 29
}

var dario = {
  nombre :'dario',
  apellido: 'jum',
  edad: 27
}

function imprimirnombreMayusculas(persona) {
var {nombre} = persona
  console.log(nombre.toUpperCase())
}
//comentarios
imprimirnombreMayusculas(dario)
imprimirnombreMayusculas(sacha)

function imprimirnombreedad(persona,edd){
  var {nombre} = persona
  var {edad} = edd
    console.log('Hola me llamo'+' ' + nombre.toUpperCase() +''+ ' tengo '+edd)
}

imprimirnombreedad(dario, 28)
imprimirnombreedad(sacha, 27)
