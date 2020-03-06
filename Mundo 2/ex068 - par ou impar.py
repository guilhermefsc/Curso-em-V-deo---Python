import random

print('=-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=-'*10)

v = 0

while True:
    jogador = int (input('Diga um valor: '))
    computador = random.randint(0,10)
    soma = jogador + computador 
    tipo = ' '
    while tipo not in 'IiPp':
        tipo = str(input('Par ou Ímpar? [P/I] ').strip().upper())[0]
    print('----'*10)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}. ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('----'*10)
    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {v} vezes.')