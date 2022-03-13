# estruturas condicionais simples e compostas

n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
m = (n1 + n2) / 2
print('sua media é {:.1f}'.format(m))
if n1 >= 6:
    print('voce foi aprovado !')
else:
    print('voce esta de recuperação')