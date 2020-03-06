from datetime import date

nascimento = int(input('Ano de nascimento: '))

print('Quem nasceu em {} tem {} em {}.'.format(nascimento, date.today().year - nascimento, date.today().year))

if date.today().year - nascimento < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - date.today().year + nascimento))
    print('Seu alistamento será em {}.'.format(nascimento+18))
elif date.today().year - nascimento > 18:
    print('Você já deveria ter se alistado há {} anos!'.format(date.today().year - nascimento - 18))
    print('Seu alistamento foi em {}.'.format(nascimento+18))
else:
    print('Você deve se alistar IMEDIATAMENTE!')