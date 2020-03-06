lista = []
pares = []
impares = []
continuar = 's'

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'nN':
        break

print('-='*30)
print(f'A lista completa é {lista}')
pares.sort()
print(f'A lista de pares é {pares}')
impares.sort()
print(f'A lista de impares é {impares}')