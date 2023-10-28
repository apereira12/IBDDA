#Faça um programa que leia um número e retorne o fatorial !

'''4! = 4 x 3 x 2 x 1'''

num = int(input('Favor informar o Número: '))
fatorial = 1
def leitorFatorial(num, fatorial):
    for i in range(num,1,-1):
        fatorial *= i

    print(fatorial)

leitorFatorial(num,fatorial)
