var miTitulo = document.querySelector('h1');
var nombre = 'maria';
var apellido = 'apellido 2';
var entero1 = 2.5633;
var entero2 = 5.6883;
miTitulo.innerHTML = 'Hello world!';

document.querySelector('h1').onclick = function() {
    alert('Ouch! Deja de pincharme!');
}

var num1 = prompt('Por favor, ingresa tu #1');
var num2 = prompt('Por favor, ingresa tu #2');

function multiplica(num1,num2) {
    var resultado = num1 * num2;
    alert (resultado);
  }

multiplica (num1,num2)