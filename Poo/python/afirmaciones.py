def primera_lista (lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type (palabra)== str, f'{palabra} no es str'
        assert len (palabra) > 0, 'no se permiten vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras

paises = ['Colombia', '', 'Chile', 4]
    print(primeras_letras(paises))