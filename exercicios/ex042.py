print('*-' * 20)
print('analisador de tipos de triangulo')
print('*-' * 20)
r1 = float(input('digite o valor da primeira reta: '))
r2 = float(input('digite o valor da segunda reta: '))
r3 = float(input('digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('as retas formam um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('as retas não podem formar um triangulo')