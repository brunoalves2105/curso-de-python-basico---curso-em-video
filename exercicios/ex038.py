a = int(input('digite um numero: '))
b = int(input('digite mais um numero: '))
if a > b:
    print('o primeiro numero {} é maior do que o segundo numero {}'.format(a, b))
elif b > a:
    print('o segundo numero {} é maior do que o primeiro numero {}'.format(b, a))
else:
    print('os numeros são iguais a {}'.format(a))