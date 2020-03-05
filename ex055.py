maior = 0
menor = 10000

for pessoa in range (1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso lido foi de {:.1f}Kg.'.format(maior))
print('O menor peso lido foi de {:.1f}Kg.'.format(menor))