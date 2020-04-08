class persona {
  constructor(nombre, apellido, altura) {
    this.nombre = nombre,
    this.apellido = apellido
    this.altura = altura
  }

saludar(fn){
  var {nombre,apellido} = this
  console.log(`Hola, me llamo ${this.nombre} ${this.apellido}`);
  if (fn){
    fn(nombre, apellido, true)
  }
}

}

class desarrollador extends persona {
  constructor(nombre, apellido, altura) {
    super(nombre, apellido, altura)

  }
}

function responderSaludo(esDev){
  var {nombre,apellido} = this
  console.log(`Hola, no se quien soy, me llamo ${this.nombre} ${this.apellido}`)
  if (esDev) {
    console.log(`eres de desarrollo ${nombre}`);
  }
}


var sacha = new persona ('sacha', 'asasxxa','1.9')
var arturo = new persona ('arturo', 'asasxxa',1.5)
var cristian = new persona ('cristian', 'asasxxa', 1.7)
var haiber = new desarrollador ('haiber', 'asasxxa',1.8)

sacha.saludar()
cristian.saludar(responderSaludo)
haiber.saludar()
arturo.saludar(responderSaludo)
