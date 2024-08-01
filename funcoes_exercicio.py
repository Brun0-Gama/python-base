# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


# def funcao_multiplica(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total


# multiplicacao = funcao_multiplica(10, 2, 3)
# print(multiplicacao)



# Criar função que fala se é par ou impar   



def impar_par (numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par!'
    return f'{numero} é impar!'

multiplo = impar_par(5)
print(multiplo)