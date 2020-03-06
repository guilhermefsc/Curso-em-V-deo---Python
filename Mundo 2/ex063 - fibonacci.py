print('--'*20)
print('Sequência de Fibonacci')
print('--'*20)
n = int(input('Quantos termos você quer mostrar? '))

contador = 4
t1 = 0
t2 = 1
t3 = t1 + t2
print('~~~'*20)
print('{} -> {} -> {}'.format(t1,t2,t3), end='')
while contador <= n:
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    contador += 1
print(' -> FIM')
print('~~~'*20)
