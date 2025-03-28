numeros = list(range(1,11))

print(numeros)

for numero in numeros:
    print('Tabuada do', numero)
    for multiplica in numeros:
        print(numero * multiplica)
    print('-' * 20)