function persona(nombre, apellido, altura) {
  this.nombre = nombre
  this.apellido = apellido
  this.altura = altura
}

persona.prototype.saludar = function () {
  console.log(`Hola, me llamo ${this.nombre} ${this.apellido}`);
}

persona.prototype.soyAlta = function () {
  if (this.altura >= 1.8){
  console.log(`Hola, soy alto ${this.nombre} ${this.apellido}`);
}else {
  console.log(`soy bajo ${this.nombre} ${this.apellido} `);
}

}

var sacha = new persona ('sacha', 'asasxxa',1.9)
var arturo = new persona ('arturo', 'asasxxa',1.5)
var cristian = new persona ('cristian', 'asasxxa', 1.7)
var haiber = new persona ('haiber', 'asasxxa',1.8)

sacha.soyAlta()
cristian.soyAlta()
sacha.saludar()
cristian.saludar()