"""tributo"""
edad = int(input('ingresa tu edad'))
ingresos = int(input('ingresa tus ingresos'))

print(ingresos)
print(edad)

if edad >= 16 and ingresos>=1000:
    print('debes pagar tributo')
else:
    print('no debes pagar')



