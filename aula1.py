#comentario
print('Hello World')
print(12, 34, end='##\n') # adicionado final de linha e o \n para pular a linha
print(12, 34, sep="-", end='##')
print(12, 34, sep='-') # sep é o separador do que eu esquevi

'''
comentario longo
pulando linha
'''

#string
print(r"testando caracter de \"escape\"") #r faz com que apareça o caracter de escape, no caso a "\"


#int
print(10)
print(-10)

#float
print(1.1, 10.11)
print(type('otavio'))

#boolean
print(10 == 10)
print(10 == 11)
print(type(10 == 10))

#coerção (converter)
print(int('1') + 1)
print(type(float('1') + 1))

#variável
nome = 'Bruno'
print(nome)