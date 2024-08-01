"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

multa = local_carro >= (LOCAL_1 - 1) and \
    local_carro <= (LOCAL_1 + 1) and \
        velocidade > RADAR_1


if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if multa:
    print('Carro multado em radar 1')
else:
    print('Carro não foi multado')