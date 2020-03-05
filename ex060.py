num = int(input('Digite um número para calcular seu fatorial: '))

total = 1
print('Calculando {}! = '.format(num), end='')
for num in range (num, 1,-1):
    print('{} x '.format(num), end='')
    total = total*num
    num -= 1

print('1 = {}'.format(total))