# verificação de categoria de natação
from datetime import date

nascimento = int(input('digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade <= 9:
    print('voce tem {} anos sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('voce tem {} anos sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('voce tem {} anos sua categoria é JUNIOR'.format(idade))
elif idade <= 25:
    print('voce tem {} anos sua categoria é SENIOR'.format(idade))
else:
    print('voce tem {} anos sua categoria é MASTER'.format(idade))
