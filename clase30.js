const API_URL = 'https://swapi.co/api/'
const PEOPLE_URL = 'people/:id'
const opts = {crossDomain: true};

conts obtenerPersonaje (id, callback) {
    const url = `${API_URL}${PEOPLE_URL.replace (':id', id)}`


$.get(url, opts, funtion (persona) {
    console.log(`hola...yo soy ${persona.name}`)
}
)
};

obtenerPersonaje(2)
obtenerPersonaje(3)
obtenerPersonaje(1)