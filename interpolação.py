"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Bruno'
preco = 100.12545
variavel = '%s o valor é R$%.2f' % (nome, preco)

print(variavel)
print('testando as interpolações %d e %x' % (1500, 1500))