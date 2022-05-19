from datetime import date
nascimento = int(input('digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('voce ainda não precisa se alistar, ainda falta {} anos'.format(saldo))
    print('seu alistamento será no ano de {}'.format(ano))
elif idade == 18:
    print('voce precisa se apresentar no exercito')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('voce deveria ter se alistado a {} anos!'.format(saldo))
    print('seu alistamento foi no ano de {}'.format(ano))