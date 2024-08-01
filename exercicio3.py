
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


# numero = input('Digite um numero inteiro: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0 #se o resto a divisão por 2 for igual a 0 quer dizer que é par
#     par_impar_str = 'Impar'

#     if par_impar:
#         par_impar_str = 'Par'

#     print(f'O numero {numero_int} é {par_impar_str}')
# else:
#     print('vc não digitou um numero inteiro')

# print('-' * 60)

# hora = input('Digite a hora em numeros inteiros: ')

# if hora.isdigit():
#     hora = int(hora)
#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <=23:
#         print('Boa noite')
#     elif hora > 23:
#         print('Essa hora não existe')
# else:
#     print('Digite apenas numeros')


# print('-' * 60)

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >4 and tamanho_nome < 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
else:
    print('Digite mais de 1 letra')