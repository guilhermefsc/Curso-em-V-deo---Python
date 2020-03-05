a = input('Primeiro segmento: ')
b = input('Segundo segmento: ')
c = input('Terceiro segmento: ')

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR triângulo ', end = '')
    if a != b != c != a:
        print('ESCALENO!')
    elif a == b == c:
        print('EQUILÁTERO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
