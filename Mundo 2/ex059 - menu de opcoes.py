x1 = int(input('Primeiro valor: '))
x2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('=-'*20)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}.'.format(x1,x2,(x1+x2)))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}.'.format(x1,x2,(x1*x2)))
    elif opcao == 3:
        print('O maior entre {} e {} é {}.'.format(x1,x2,max(x1,x2)))
    elif opcao == 4:
        print('Informe os números novamente:')
        x1 = int(input('Primeiro valor: '))
        x2 = int(input('Segundo valor: '))
    else:
        opção = int(input('Opção inválida. Tente novamente: '))


print('Fim do programa, volte sempre!')