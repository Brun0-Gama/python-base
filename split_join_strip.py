"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = 'Olha só, que interessante'
lista = frase.split()
lista_frase = frase.split(', ')
print(lista) #listou conforme os espaços, porém levou a virgula junto no "só"
print(lista_frase) #listou conforme a virgula

for i, frase in enumerate(lista_frase):
    print(lista_frase[i].strip()) #strip tira os espaços no começo e final da string, rstrip (corta so da direita) lstrip(só da esquerda)

