#Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. Ao final deve mostrar a quantidade de vitórias
import random
def VerificaPar():
   numero = random.randint(1, 100)
   if numero % 2 == 0:
       return 2
   else:
       return 1

def calculo(y):

    Ntermos = -1
    while True:
        numero = random.randint(1, 100)
        if numero % 2 == 0:
            y = 2
        else:
            y = 1
        Ntermos += 1
        x = int(input('Digíte 1 para escolher ímpar e 2 para escolher par: '))
        if x != y:
         break
    return f'O Número final era {numero} e você acertou outras {Ntermos}  vezes'





y = VerificaPar()
print(calculo(y))


