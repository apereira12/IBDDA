#Crie um programa onde serão informados diversos valores em uma lista. Caso o número já
# exista ele não será adicionado. No final, serão exibidos todos os valores únicos em ordem crescente

def valores():
   listaValores = []
   print('Favor digitar os números que deseja e digite "0000" para parar')
   try:
       while True:
           valor = input('Favor informar o número: ')
           if valor == '0000':

               break
           else:
                if int(valor) not in listaValores:
                    listaValores.append(int(valor))
   except ValueError:
       print('Favor digitar apenas números')
   listaValores.sort()
   print('Os números da lista em ordem são:')
   for i in listaValores:
       print(i)

valores()


