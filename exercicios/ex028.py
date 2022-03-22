from random import randint
from time import sleep

a = randint(0,5)
print('*** jogo do adivinha ***')
e = int(input('tente acertar o numero escolhido de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
print('numero escolhido: {}'.format(a))
if a == e:
    print('voce acertou PARABENS :)'.format(a))
else:
    print('PC ganhou :´('.format(a))