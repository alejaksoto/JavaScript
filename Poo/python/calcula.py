def run(): 
    print ('calculadora de divisas')
    print('convierte divisas')
    print('')

    divisa = int(input('Ingrese la divisa, 1:euro, 2:dollar, 3:mex'))

    if (divisa == 1 ):
        ammount = int(input('ingrese la cantidad'))
        rate = 4000
        result = rate * ammount
        print('${} pesos ${} son ${} pesos colombianos'.format(ammount,divisa, result))
        print(' ')

    elif (divisa == 2):
        ammount = int(input('ingrese la cantidad'))
        rate = 3899
        result = rate * ammount
        print('${} pesos ${} son ${} pesos colombianos'.format(ammount,divisa, result))
        print(' ')
    
    else: 
        ammount = int(input('ingrese la cantidad'))
        rate = 389
        result = rate * ammount
        print('${} pesos ${} son mexicanos pesos colombianos'.format(ammount,divisa, result))
        print(' ')

if __name__ == '__main__':
    run()