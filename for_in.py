# senha = '123456'
# digite_senha= ''
# repeticao = 0

# while digite_senha != senha:
#     digite_senha = input(f'Acerte a senha ({repeticao}x): ')

#     repeticao += 1

# print(repeticao)
# print('Laço infinito')



texto = 'Bruno'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'

print(novo_texto + '*')