"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    #definição
    print(f'{x=} , y={y}', '|' 'x + y = ', x + y)

soma(1, 2)
soma(y=2, x=1) 



# Caso vc tenha um argumento sem valor


def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} , y={y} , {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(1, 2, 3) 
