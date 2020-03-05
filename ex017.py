import math
cop = float(input('Comprimento do cateto oposto: '))
cad = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir: {:.2f}.'.format(math.sqrt(cop**2+cad**2)))
#print('A hipotenusa vai medir: {:.2f}.'.format(math.hypot(cop,cad)))