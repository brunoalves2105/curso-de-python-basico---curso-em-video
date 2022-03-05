dia = int(input('quantos dias de aluguel ? '))
km = float(input('quantos quilometros rodados ? '))
total = (dia * 60) + (km * 0.15)
print('o valor a ser pago é de R${:.2f}'.format(total))