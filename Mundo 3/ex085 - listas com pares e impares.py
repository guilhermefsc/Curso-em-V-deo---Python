lista = []
pares = []
impares = []

for valor in range(0,7):
    lista.append(int(input(f'Digite o {len(lista)+1}º valor: ')))
    if lista[valor] % 2 == 0:
        pares.append(lista[valor])
    elif lista[valor] % 2 == 1:
        impares.append(lista[valor])

print('-='*30)
pares.sort()
print(f'Os valores pares digitados foram: {pares}')
impares.sort()
print(f'Os valores ímpares digitados foram: {impares}')
 
'''
lista = [[], []]

for c in range(1, 8):
	n = int(input(f'Informe o {c}° Valor:  '))
	if n % 2 == 0:
		lista[0].append(n)
	else:
		lista[1].append(n)

print('-=' * 15)
print(f'Os PARES são: {sorted(lista[0])}')
print(f'Os ÍMPARES  são: {sorted(lista[1])}')
'''