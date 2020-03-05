print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = input('Primeiro segmento: ')
b = input('Segundo segmento: ')
c = input('Terceiro segmento: ')

if a<b+c and b<a+c and c<a+b:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
