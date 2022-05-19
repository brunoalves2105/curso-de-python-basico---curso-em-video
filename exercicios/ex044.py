print('{:=^40}'.format(' LOJAS SIMPLICIO '))
print(''' FORMAS DE PAGAMENTO
[1] - avista dinheiro/cheque - 10% de desconto'
[2] - avista cartão - 5% de desconto'
[3] - parcelado em 2x no cartão - preço normal'
[4] - parcelado em 3x ou mais no cartão - 20% de juros''')
cobrar = float(input('digite o valor a ser cobrado: '))
opcao = int(input('digite a forma de pagamento: '))
if opcao == 1:
    cobrar = cobrar - (cobrar * 10 / 100)
    print('o valor a ser pago é {:.2f} voce tera 10% de desconto por pagar avista em dinheiro ou cheque'.format(cobrar))
elif opcao == 2:
    cobrar = cobrar - (cobrar * 5 / 100)
    print('o valor a ser pago é R${:.2f} voce tera 5% de desconto por pagar avista no cartão'.format(cobrar))
elif opcao == 3:
    parcela = cobrar / 2
    print('o valor a ser pago é R${:.2f} voce pagará 2x parcelas de R${:.2f} sem juros'.format(cobrar, parcela))
elif opcao == 4:
    cobrar = cobrar + (cobrar * 20 / 100)
    qtdparc = int(input("qual será a quantidade de parcelas ? "))
    parcelas = cobrar / qtdparc
    print('o valor a ser pago é R${:.2f} com 20% de juros em {}x parcelas de R${:.2f}!'.format(cobrar, qtdparc, parcelas))
else:
    print("voce digitou uma opção invalida, tente novamente !")