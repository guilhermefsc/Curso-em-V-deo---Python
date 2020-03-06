l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l,h,l*h))
print('Para pintar essa parede você precisará de {:.4f}l de tinta.'.format(l*h/2))