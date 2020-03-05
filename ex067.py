n = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('---'*10)
    if n < 0:
        break  

    for x in range(1,11):
        print(f'{n} x {x} = {n*x}')
    print('---'*10)
   
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

