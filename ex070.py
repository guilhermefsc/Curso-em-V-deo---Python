print('----'*10)
print('       LOJA SUPER BARATÃO')
print('----'*10)

prodbarato = ' '
custobarato = 99999999
soma = 0
caro = 0

while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    soma += valor
    if valor > 1000:
        caro += 1
    if valor < custobarato:
        prodbarato = nome
        custobarato = valor
    continuar = ' '
    if continuar not in 'SsNn':
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break

print('-------- FIM DO PROGRAMA --------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {caro} custando mais de R$1000.00')
print(f'O produto mais barato foi {prodbarato} que custa R${custobarato:.2f}')