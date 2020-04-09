const API_URL = 'https://swapi.co/api/'
const PEOPLE_URL = 'people/:id'
const opts = {crossDomain: true}

const onRespnse = function (luke) {
  console.log (`hola yo soy, ${luke.name}`)
}   

function obtenerPersonaje (id) {
  const url = `${API_URL}${PEOPLE_URL.replace (':id', id)}`
  $.get(url, opts, onRespnse)
}
