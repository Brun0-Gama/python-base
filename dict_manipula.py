# Manipulando chaves e valores em dicionários

pessoa = {}

pessoa['nome'] = 'Luiz'
# pessoa['sobrenome'] = 'Otavio'

print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])