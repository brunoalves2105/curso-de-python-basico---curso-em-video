altura = float(input('digite a altura da parede: '))
largura = float(input('digite a largura da parede: '))
area = float(largura * altura)
tinta = float(area / 2)
print('com a medida de {}x{} a area para pintura é de {}m² \n para pintar voce vai precisar de {} litros de tinta'.format(altura, largura, area, tinta))