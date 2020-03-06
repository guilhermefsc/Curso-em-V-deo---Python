expr = str(input('Digite a expressão: '))
lista = list(expr)

abre = 0
fecha = 0

while '(' in lista:
    lista.remove('(')
    abre += 1 
while ')' in lista:
    lista.remove(')')
    fecha += 1 


if abre == fecha:
    print('Sua expressão está VÁLIDA!')
elif abre != fecha:
    print('Sua expressão está ERRADA!')