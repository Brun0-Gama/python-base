#precedência entre os operadores na ordem

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 # de cabeça ficaria 2 ** 10 = 1024, porém o resultado vai dar 7
print(conta_1)

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)