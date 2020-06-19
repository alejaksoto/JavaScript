contra = ('thor')
password = str(input('cual es tu contraseña'))

if contra == password.lower():
    print('las contraseñas son iguales')
else:
    print('Son diferentes')