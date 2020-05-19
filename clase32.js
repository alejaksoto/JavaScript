const API_URL = 'https://swapi.co/api/'
const PEOPLE_URL = 'people/:id'

const opts = {crossDomain: true}

function obtenerPersonaje (id) {
    return new Promise ( (resolve, reject) => {
        const url = `${API_URL}${PEOPLE_URL.replace (':id', id)}`
    $
        .get(url, opts, function (data){
            resolve (data)
        })
        .fail (() => reject (id))
    })
        
}

function onError (id){
    console.log(`sucedio un error al obtener el persnaje ${id}`)
}

obtenerPersonaje (1)
    .then (personaje => {
        console.log (`el personaje es 1 ${personaje1.name}`)
        return obtenerPersonaje (2)
    })
.then (personaje2 => {
    console.log (`el personaje es 2 ${personaje2.name}`)
    return obtenerPersonaje (3)
})
.then (personaje3 => {
    console.log (`el personaje es 3 ${personaje3.name}`)
    return obtenerPersonaje (4)
})
.then (personaje4 => {
    console.log (`el personaje es 4 ${personaje4.name}`)
    return obtenerPersonaje (5)
})
.catch (onError)