contador = 0
contadorext = 0

while contadorext <5:
    while contador < 6:
        print(contador, contadorext)
        contador +=1

        if contador >=3: 
            break
    contadorext +=1
    contador=0
