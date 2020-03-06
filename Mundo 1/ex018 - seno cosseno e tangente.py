import math

x = float(input('Digite o ângulo que você deseja: '))

print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(x,math.sin(math.radians(x))))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(x,math.cos(math.radians(x))))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(x,math.tan(math.radians(x))))