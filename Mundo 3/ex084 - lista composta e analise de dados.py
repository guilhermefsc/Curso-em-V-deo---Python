pessoa = []
lista = []
maior = menor = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar not in 'sS':
        break

'''
nomes = []
pesos=[]

for p in lista:
    nomes.append(p[0])
    pesos.append(p[1])
'''

print('-='*30)
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if maior == p[1]:
        print(f'[{p[0]}] ',end='')
print()    
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in lista:
    if menor == p[1]:
        print(f'[{p[0]}] ', end='')
        