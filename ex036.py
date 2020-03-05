casa = float(input('casa da casa: R$'))
salario  = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa/(anos*12)
print('Para pegar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa,anos,prestacao))

if prestacao >= 0.30*salario:
    print('Empréstimo NEGADO!')
else: 
    print('Empréstimo pode ser CONCEDIDO!')