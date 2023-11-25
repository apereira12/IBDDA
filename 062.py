#Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes das duas listas.
# Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].

def listas():
   listaA = []
   listaB = []
   while len(listaA) < 5:
       x = int(input('Favor informar os Números da primeira lista: '))
       listaA.append(x)
   while len(listaB) < 5:
       y = int(input('Favor informar os Números da segunda lista: '))
       listaB.append(y)

   z = list(map(sum, zip(listaA, listaB)))

   print(z)

listas()

