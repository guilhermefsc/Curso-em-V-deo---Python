mais18 = 0
homens = 0
mulhermenos20 = 0

while True:
    sexo = ' '
    continuar = ' '
    print('---'*10)
    print('     CADASTRE UMA PESSOA')
    print('---'*10)

    idade = int(input('Idade: '))
    if idade > 18:
        mais18 += 1
    
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'Mm':
            homens += 1
        elif idade < 20:
            mulhermenos20 += 1

    print('---'*10)
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    
print('\n')
print(f'Total de pessoas com mais de 18 anos: {mais18}.')
print(f'Ao total temos {homens} homens cadastrados.')
print(f'E temos {mulhermenos20} mulheres com menos de 20 anos.')