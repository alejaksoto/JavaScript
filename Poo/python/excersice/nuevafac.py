def run(numero):
    
    if numero<1: 
        print('no es positivo')
    elif numero == 1:
        return 1
    return numero * run (numero-1)

numero = int(input('ingrese el numero'))
print(run(numero))

