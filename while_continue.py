
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador +=1

    if contador == 6:
        print("Pulei o 6")
        continue

    if contador >=10 and contador <= 15:
        print("Pulei o", contador)
        continue

    print(contador)

    if contador == 20:
        break