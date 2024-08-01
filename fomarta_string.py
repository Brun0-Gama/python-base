nome = 'Bruno'
altura = 1.70
peso = 68.5
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu IMC é')
print(imc)

print('#####################')

print('Agora usando o "f" que é o "f-strings"')

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
