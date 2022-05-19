from random import randint
from time import sleep
print('{:=^40}'.format(' JOGO JOKENPO '))
print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = int(input('escolha sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
print('=*' * 20)
print('jogador escolheu {}'.format(itens[jogador]))
computador = randint(0, 2)
print('computador escolheu {}'.format(itens[computador]))
print('=*' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE !')
    if jogador == 1:
        print('COMPUTADOR VENCEU !')
    if jogador == 2:
        print('JOGADOR VENCEU')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU !')
    if jogador == 1:
        print('EMPATE !')
    if jogador == 2:
        print('JOGADOR VENCEU !')
if computador == 2:
    if jogador == 0:
        print("JOGADOR VENCEU !")
    if jogador == 1:
        print('COMPUTADOR VENCEU !')
    if jogador == 2:
        print('EMPATE !')