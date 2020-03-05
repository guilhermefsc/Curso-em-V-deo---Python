d = int(input("Uma distância em metros: "))

print('A medida de {:.1f}m corresponde a '.format(d))
print('{:.3f}km'.format(d/1000))
print('{:.2f}hm'.format(d/100))
print('{:.1f}dam'.format(d/10))
print('{}dm'.format(d*10))
print('{}cm'.format(d*100))
print('{}mm'.format(d*1000))