n = int(input('Digite um número para ver sua tabuada: '))
a = 1
print("------------")
while(a<=10):
   print('{} x {:2} = {}'.format(n,a,(n*a)))
   a = a + 1
print("------------")