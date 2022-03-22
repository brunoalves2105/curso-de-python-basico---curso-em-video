vel = int(input('qual sua velocidade ? '))
m = 0
if vel > 80:
    m = (vel - 80) * 7
    print('voce passou a {}km/h ultrapassou a velocidade minima de 80km/h sua multa será de R${:.2f}'.format(vel, m))
else:
    print('voce passou a {}km/h boa viagem :)'.format(vel))