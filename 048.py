#Crie um programa que pede ao usuário para digitar dois números e, em seguida, divide o primeiro número pelo segundo número. No entanto,
# o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.
def funcao():
   while True:
       try:
           num1 = int(input('Favor informar o numerador: '))
           num2 = int(input('Favor informar o denominador: '))
           if num2 == 0:
               print('Divisão por zero não permitida')
               continue
           divisao = num1/num2
           break
       except ValueError:
           print('Você está vacilando, tem que colocar número')
   print(f'Sua divisão é {divisao}')

funcao()