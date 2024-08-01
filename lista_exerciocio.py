"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['eu', 'vc', 'ele']
lista.append('nós') #se colocar depois da linha 12 não funciona

indices = range(len(lista))


#print(indices)


for indice in indices:
    indice_lista = lista[indice]
    print(indice, indice_lista, type(indice_lista))