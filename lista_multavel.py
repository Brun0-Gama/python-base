"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]

# numero = lista[2]

# lista[2] = 300
# del lista[2]
# print(lista)
# print(numero)
# print(lista[2])

lista.append(50)
ultimo_valor = lista.pop()
lista.append(60)
lista.append(70)

print(lista, 'removido o', ultimo_valor)
print('#######################')


#          0   1   2   3
lista_1 = [10, 20, 30, 40]

del lista_1 [-1]
# lista_1 .clear()
lista_1 .insert(100, 5)
print(lista_1)
print(lista_1 [3])


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)
print(lista_a)