from datetime import date
ano = int(input('digite o ano que deseja analisar: para analisar o ano atual digite 0 '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(' o ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} não é BISSEXTO'.format(ano))