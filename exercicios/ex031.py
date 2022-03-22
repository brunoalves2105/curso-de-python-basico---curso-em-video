viagem = int(input('digite quantos km sera sua viagem: '))
pas = 0
if viagem <= 200:
    pas = viagem * 0.5
    print('o valor da sua passagem sera R${:.2f}'.format(pas))
else:
    pas = viagem * 0.45
    print('o valor da sua passagem sera R${:.2f}'.format(pas))