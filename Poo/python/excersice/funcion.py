
def run ():
    programa = int(input('cual programa quieres ejecutar 1:binario; 2: aproximacion'))
    if programa == 1:
        binaria()
    elif programa == 2:
        aproximacion ()

def binaria():
    objetivo = int(input('ingresa el objetivo'))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/ 2
    while abs (respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo=respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) /2
    
    print(f'la raiz cuadrada del {objetivo} es {respuesta}')

def aproximacion():
    objetivo = int(input('escoge un numero'))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0 

    while abs(respuesta **2 - objetivo)>= epsilon and respuesta <= objetivo:
        respuesta+= paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'nos se encontro la raiz cuadra de {objetivo}')
    else:
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')


if __name__ == "__main__":
    run()