print('Gerador de PA')
print('-='*10)

a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end = '')
        termo += r
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total))
