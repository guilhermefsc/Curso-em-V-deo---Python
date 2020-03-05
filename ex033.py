v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

if v1 < v3 and v1 < v2:
    print('O menor valor digitado foi {}'.format(v1))
elif v2 < v1 and v2 < v3:
    print('O menor valor digitado foi {}'.format(v2))
else:
    print('O menor valor digitado foi {}'.format(v3))

if v1 > v3 and v1 > v2:
    print('O maior valor digitado foi {}'.format(v1))
elif v2 > v1 and v2 > v3:
    print('O maior valor digitado foi {}'.format(v2))
else:
    print('O maior valor digitado foi {}'.format(v3))


