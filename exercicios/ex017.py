import math
catOp = float(input('digite o valor do cateto oposto: '))
catAd = float(input('digite o valor do cateto adjacente: '))
#hi = (catOp ** 2 + catAd ** 2) ** (1/2)
hi = math.hypot(catOp, catAd)
print('sabendo que o valor do cateto oposto é {:.2f} \no valor do cateto adjacente é {:.2f} \no valor da hipotenusa é {:.2f}'.format(catOp, catAd, hi))