import math
angulo = float(input('digite o valor do angulo: '))
sen = math.sin(math.radians(angulo))
print('o angulo de {}° tem o seno de {:.2f}'.format(angulo, sen))
cos = math.cos(math.radians(angulo))
print('o angulo {}° tem o cosseno de {:.2f}'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('o angulo de {}° tem a tangente de {:.2f}'.format(angulo, tan))
