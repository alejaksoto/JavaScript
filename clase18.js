var Daniel = {
    nombre: `Daniel`,
    apellido: `Dominguez`,
    altura: 1.82
}
var Paula = {
    nombre: `Paula`,
    apellido: `Torres`,
    altura: 1.70
}
var Juan = {
    nombre: `Juan`,
    apellido: `Lopez`,
    altura: 2.00
}
var Arturo = {
    nombre: `Arturo`,
    apellido: `Tello`,
    altura: 1.75
}
var Diana = {
    nombre: `Diana`,
    apellido: `Medina`,
    altura: 1.60
}

var personas = [Daniel, Paula, Juan, Arturo, Diana];

const esAlta = ({ altura }) => altura > 1.8

var personasAltas = personas.filter (esAlta)

const pasarAlturaCMS = persona => {
  //personas.altura *= 100
  return {
    ...personas,
    altura :persona.altura * 100
  }
}

var personasCMs = personas.map(pasarAlturaCMS)

const reducer = (acum, personas) =>
acum + totaldeLibros

var totaldeLibros = personas.reduce (reducer, 0)

console.log(totaldeLibros);
