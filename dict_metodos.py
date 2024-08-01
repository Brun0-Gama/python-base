# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'Antonio',
}

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# pessoa.setdefault('idade', 20)
# print(pessoa['idade'])

# for valor in pessoa.values():
#     print(valor)

# for chaves, valor in pessoa.items():
#     print(chaves, valor)

import copy


d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

print(d1)

d2 = copy.deepcopy(d1) #aqui ele entra em todos os subniveis

#d2 = d1.copy()
d2['c1'] = 100
d2['l1'][1] = 9 #ele alterou no d1 tbm, para não alterar precisa usar o modulo copy

print(d1)
print(d2)