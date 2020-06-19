frase=input("Frase:")
nueva=""
i=len(frase)-1
while i>=0:
    nueva=nueva+frase[i]
    i= i-1
print(nueva)