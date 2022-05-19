salario = float(input('digite o valor do seu salario atual: '))
valorImovel = float(input('digite o valor do imovel a ser financiado: '))
anos = int(input('digite em quantos anos deseja pagar: '))
valorParcela = valorImovel / (anos * 12)
porcentagem = salario - (salario * 70 / 100)
if valorParcela <= porcentagem:
    print('seu emprestimo foi aprovado, voce pagara R${:.2f} por mes'.format(valorParcela))
else:
    print('seu financiamento foi negado pois o valor da parcela de R${:.2f} ultrapassa 30% do seu salario'.format(valorParcela))