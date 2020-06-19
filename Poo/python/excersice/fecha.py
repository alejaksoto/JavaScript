cadena = int(input("ingresa un  numero de 8 digitos"))
año = cadena%10000
dia = cadena// 1000000
mes= (cadena//10000)%100 

print(dia,"/", mes,"/",año)
