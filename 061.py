#Escreva um programa que crie uma lista vazia e permita que o usuário
# insira números nessa lista até que ele digite um número negativo. Em seguida, exiba a lista na tela.

def valores():
   listaValores = []
   print('Favor digitar os números que deseja e digite "0000" para parar')
   try:
       while True:
           valor = int(input('Favor informar o número: '))
           if valor < 0:
               break
           else:
                if int(valor) not in listaValores:
                    listaValores.append(int(valor))
   except ValueError:
       print('Favor digitar apenas números')
   print('Os números da lista são:')
   for i in listaValores:
       print(i)

valores()