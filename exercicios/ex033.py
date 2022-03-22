n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
n3 = int(input('digite o terceiro valor: '))
# verificando menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('o menor numero é {}'.format(menor))
print('o maior numero é {}'.format(maior))