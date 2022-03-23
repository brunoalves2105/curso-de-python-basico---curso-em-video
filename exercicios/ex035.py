print('*-' * 20)
print('Analisador de triangulo')
print('*-' * 20)
r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('as retas podem FORMAR UM TRIANGULO!')
else:
    print('as retas NÃO PODEM formar um triangulo!')
conta = 3 * 5 + 4 ** 2
print(conta)