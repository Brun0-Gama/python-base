"""
Closure e funções que retornam outras funções
"""


# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar


# falar_bom_dia = criar_saudacao('Bom dia')
# falar_boa_noite = criar_saudacao('Boa noite')

# for nome in ['Maria', 'Joana', 'Luiz']:
#     print(falar_bom_dia(nome))
#     print(falar_boa_noite(nome))



def funcao_saudacao(saudacao):
    def nome_fulano(nome):
        return f'{saudacao}, {nome}!'
    return nome_fulano

v_saudacao = funcao_saudacao('Bom dia')

for fulano in ['Bruno', 'José']:
    print(v_saudacao(fulano))    