class persona {
  constructor(nombre, apellido, altura) {
    this.nombre = nombre,
    this.apellido = apellido
    this.altura = altura
  }

saludar(fn){
  console.log(`Hola, me llamo ${this.nombre} ${this.apellido}`);
  if (fn){
    fn(this.nombre, this.apellido, true)
  }
}


soyAlta(){
  return this.altura > 1.8
}
}

class desarrollador extends persona {
  constructor(nombre, apellido, altura) {
    super(nombre, apellido, altura)

  }
  saludar(fn){
    var nombre = this.nombre
    var apellido = this.apellido
    console.log(`Hola, desarrollador, me llamo ${this.nombre} ${this.apellido}`);
    if (fn){
      fn(this.nombre, this.apellido, true)
    }

  }
}

function responderSaludo(esDev){
  console.log(`Hola, desarrollador, me llamo ${this.nombre} ${this.apellido}`)
  if (esDev) {
    console.log(`eres de desarrollo`);
  }
}


var sacha = new persona ('sacha', 'asasxxa','1.9')
var arturo = new persona ('arturo', 'asasxxa',1.5)
var cristian = new persona ('cristian', 'asasxxa', 1.7)
var haiber = new desarrollador ('haiber', 'asasxxa',1.8)

sacha.saludar(responderSaludo)
cristian.saludar(responderSaludo)
haiber.saludar(responderSaludo)
arturo.saludar(responderSaludo)
