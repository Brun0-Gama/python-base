# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def funcao_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplica = funcao_multiplicador(2)
triplica = funcao_multiplicador(3)

print(duplica(5))
print(triplica(5))