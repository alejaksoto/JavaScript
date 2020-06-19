def hello():
    age = int(input('ingrese la edad'))
    if age< 10:
        print('hola niño')
    else: 
        print ('hola adulto')

if __name__ == '__main__':
    hello()