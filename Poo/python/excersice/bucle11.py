"""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la
 palabra introducida empezando por la última."""

n =input('introduce una palabra')
lon=len(n)
for i in range((lon-1), -1, -1):
    print(n[i])

