n = int(input('Digite um número: '))

cont = 0
for c in range(1, n+1):
    if n % c == 0: 
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO número {} foi divisível {} vezes, por isso ele '.format(n,cont), end='')

if cont == 2 or cont == 1:
    print('\033[32mÉ PRIMO!')
else:
    print('\033[31mNÃO É PRIMO!\033[m')