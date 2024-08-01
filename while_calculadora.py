# Caculadora com While

while True:

    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite um numero: ')
    operador = input('Digite um operador (+, -, /, *): ')

    numeros_validos = None

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Algum numero invalido!')
        continue

    operadores_permitido = "+-/*"

    if operador not in operadores_permitido:
        print('Operador invalido!')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador.')
        continue

    if operador == '+':
        print(f'{numero_1_float}+{numero_2_float} =', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float}-{numero_2_float} =', numero_1_float - numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float}/{numero_2_float} =', numero_1_float / numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float}*{numero_2_float} =', numero_1_float * numero_2_float)
    else:
        print('Ué!')
        
    sair = input('Vc deseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
