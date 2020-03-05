import math
x = float(input('Digite um valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}.'.format(x,math.trunc(x)))
#print('O valor digitado foi {} e a sua porção inteira é {}.'.format(x,int(x)))
print('O valor digitado foi {} e a sua porção decimal é {:.2f}.'.format(x,x-math.trunc(x)))
#print('O valor digitado foi {} e a sua porção decimal é {:.2f}.'.format(x,x-int(x)))