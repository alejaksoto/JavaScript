const API_URL = 'https://swapi.co/api/';
const PEOPLE_URL = 'people/:id';
const opts = {crossDomain: true};

conts onPeopleResponse = funtion (persona) {
    console.log(`hola soy, ${persona.name}`)
};

funtion obtenerPersonaje (id) {
    const url = `${API_URL}${PEOPLE_URL.replace (':id', id)}`
    $.get(url, opts, onPeopleResponse)
};

obtenerPersonaje(2)
obtenerPersonaje(3)
obtenerPersonaje(1)