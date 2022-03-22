salario = float(input('qual seu salario atual ?: '))
if salario <= 1250:
    print('seu salario com 15% de aumento fica em {:.2f}'.format(salario * 1.15))
if salario > 1250:
    print('seu salario com 10% de aumento fica em {:.2f}'.format(salario * 1.10))