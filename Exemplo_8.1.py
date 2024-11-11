n = -1

while n != 0:

    n = int(input('Digite um inteiro: '))
    
    match n: 
        case 1 :
            print('     você digitou um')
        case 2:
            print('     você digitou dois')
        case 3:
            print('     voce digitou três')
        case _:
            print('     voce digitou outra coisa')

print(' Fim do Programa')