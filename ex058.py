from random import randint

computador = randint(0,10)

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

jogador = int(input('Qual é o seu palpite? '))

while jogador not in range(0,10):
    jogador = int(input('Paplite inválido. Digite um número entre 0 e 10: '))

cont = 1

while jogador != computador:
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
        cont += 1
        jogador = int(input('Qual é o seu palpite? '))
    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
        cont += 1
        jogador = int(input('Qual é o seu palpite? '))

print('Acertou com {} tentativas. Parabéns!'.format(cont))