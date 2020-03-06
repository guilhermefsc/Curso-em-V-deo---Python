continuar = 's'
lista= []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:    
        lista.append(n)
        print('Valor adicionado com sucesso...')
    
    continuar = str(input('Quer continuar? [S/N] ')).strip()
    if continuar in 'nN':
        break
print('-='*30)
lista.sort()
sorted
print(f'Você digitou os valores {lista}')