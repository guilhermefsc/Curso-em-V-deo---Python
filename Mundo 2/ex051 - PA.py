print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30)

a = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for x in range(0,10):
    print('{} -> '.format(a), end ='')
    a += r
print('ACABOU')