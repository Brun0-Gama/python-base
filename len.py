"""
Fatiamento de strings
 012345678 -> indice
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'olá mundo'
# print(variavel[4]) #somente o ponto que eu quero
# print(variavel[4:8]) #ponto inicial até onde eu quero que ele vá
# print(variavel[4:]) #ponto inicial até o final
# print(variavel[:4]) #Do inicio até onde eu quero que vá

#Funcão len
print(len(variavel)) #mostra o total de caracteres
print(variavel[0:9:1]) #ordem: inicio, fim, e de quanto em quanto vai pular
print(variavel[0:9:2])
print(variavel[::2])