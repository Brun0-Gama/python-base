# count é um interador

from itertools import count

numero = count()
numero_2 = range(10)

for x in numero:
    if x >= 10:
        break

    print(x)

print()    

for x in numero_2:
    if x > 10:
        break

    print(x)