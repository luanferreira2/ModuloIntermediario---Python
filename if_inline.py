## uso comum do if

x = 10
y = 10
if x >= y:
    print(x)
else:
    print(y)


## uso do if inline

print('-------------------------------')

print(x) if x >= y else print(y)  ## else é obrigatorio
                                  ## não é preciso dois pontos

print(f'O valor de x é {x}') if x >= y else print(f' O valor de y é {y}')


