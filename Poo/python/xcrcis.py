"""divide la cuenta
cuantas personas dividen la cuenta
% de propina a incluir
% de impuestos
total de valor por cada uno"""

person = int(input('Cantidad de personas'))
porcent = int(input('porcentaje de propina'))
porcent = porcent/1000
impuesto = 0.05

cena=int(input('cual es el valor de la cena'))

cuenta = (cena/person)
porcent = cuenta*porcent
impuesto = cuenta*impuesto
cuenta = cuenta+porcent+impuesto

print(f'LA cuenta que debe pagar cada uno es{cuenta}')