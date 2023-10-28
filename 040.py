#Escreva um programa que leia um número n inteiro qualquer e
# mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

#Fórmula : Fn = Fn - 1 + Fn - 2
'''num = int(input('Favor informar o Número: '))

def rec_fib(n):
    if n > 1:
        return rec_fib(n - 1) + rec_fib(n - 2)
    return n


for i in range(num):
    print(rec_fib(i))'''

'''num = int(input('Favor informar o Número: '))'''

num = int(input('Favor informar o Número: '))

#Primeiros num

a = 0
b = 1

for i in range(num):

    print(a)

    a, b = b, a + b
