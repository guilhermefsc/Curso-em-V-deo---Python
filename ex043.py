peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura (m) '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}.'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO, cuidado!')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está na faixa de PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else: 
    print('Você está em OBESIDADE MÓRBIDA, CUIDADO!')