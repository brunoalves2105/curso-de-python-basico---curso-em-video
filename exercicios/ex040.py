# avaliação do aluno

n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
media = (n1 + n2) / 2
print('com a nota {:.1f} e {:.1f} a media do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('o aluno esta REPROVADO!'.format(media))
elif 7 > media >= 5:
    print('o aluno esta de RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('o aluno esta APROVADO!'.format(media))