codigos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista = []
lista2 = []

print(' Uso de if convencional:')

for codigo in codigos:
    if( codigo > 3 and codigo < 8):

        lista.append(codigo)

print(' Codigos filtrados --> ',lista)

print('\n\n Uso de inline if: ')

for codigo in codigos:
    lista2.append(codigo) if codigo > 3 and codigo < 8 else 0

print(' Códigos filtrados --> ', lista2)