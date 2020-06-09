text = input("Ingrese texto:")
numerotext = int(len(text))

print(text[0])
indice = int(input('Ingrese nuevo numero'))
if numerotext <= indice:
    print('Este numero no sirve')
else:
    print(text[indice])
