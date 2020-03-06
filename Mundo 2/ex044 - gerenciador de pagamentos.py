print('=========== LOJAS GUANABARA ===========')
compra = float(input('Preço das compras: R$'))
opcao = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))

if opcao == 1:
    total = 0.9*compra
elif opcao == 2:
    total = 0.95*compra
elif opcao == 3:
    total = compra
    print('Sua compra será parcelada em 2x de R${:.2f}, SEM JUROS.'.format(compra/2))
elif opcao == 4:
    total = 1.20*compra
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f}, COM JUROS.'.format(parcelas, total/parcelas))

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra,total))