primeiro_valor = input('Digite o valor: ')
segundo_valor = input('Digite outro valor: ')

# if primeiro_valor > segundo_valor:
#     print('Primeiro valor é maior que o segundo valor digitado')
# elif segundo_valor > primeiro_valor:
#     print('Segundo valor é maior que o primeiro valor digitado')
# else:
#     print('Os valores do primeiro e segundo são iguais')


if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor} é maior que o {segundo_valor}'
    )
elif segundo_valor > primeiro_valor:
    print(
        f'{segundo_valor} é maior que o {primeiro_valor}'
    )
else:
    print(
        f'{segundo_valor} é igual a {primeiro_valor} '
    )