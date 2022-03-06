import math
catOp = float(input('digite o valor do cateto oposto: '))
catAd = float(input('digite o valor do cateto adjacente: '))
hipot = math.hypot(catOp, catAd)
print('sabendo que o valor do cateto oposto é {:.3f} \no valor do cateto adjacente é {:.3f} \no valor da hipotenusa é {:.3f}'.format(catOp, catAd, hipot))