velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Multado! Você excedeu o limite de 80Km/h. Sua multa é de R${:.2f}'.format((velocidade - 80)*7))