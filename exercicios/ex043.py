peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('seu imc é {:.1f} voce esta ABAIXO do peso ideal, procure um medico!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('seu imc é {:.1f} voce esta no peso ideal, PARABENS!'.format(imc))
elif imc > 25 and imc <= 30:
    print('seu imc é {:.1f} voce esta em SOBREPESO, se cuida!'.format(imc))
elif imc > 30 and imc <= 40:
    print('seu imc é {:.1f} voce esta OBESO, se cuida!'.format(imc))
elif imc > 40:
    print('seu imc é {:.1f} voce esta com OBESIDADE MORBIDA, procure um medico!'.format(imc))