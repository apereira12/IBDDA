#Escreva um programa que tenha uma função, verifica_par(), que receba um número e verifique se é par
def verifica_par(x):
    if x % 2 !=0:
        return 'O número é ímpar'
    else:
        return 'O número é par'

def valor():
    try:
        x = int(input('Favor informar o valor: '))
        return x
    except ValueError:
        print('Só aceitamos números')
        exit()


x = valor()
print(verifica_par(x))


