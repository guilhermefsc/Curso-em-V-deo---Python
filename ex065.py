op = 'S'
soma = 0
maior = -999999999999
menor = 9999999999999
contador = 0

while op == 'S':
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    contador += 1
    op = str(input('Quer continuar? [S/N] ')).strip().upper()

soma = soma/contador
print('Você digitou {} números e a média foi {}.'.format(contador,soma))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))

