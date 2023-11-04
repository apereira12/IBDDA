#Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000.
# No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)

def calculo():
    x = int(input('Favor informar o valor: '))
    Ntermos = 1
    continuar = ''

    while True:
        y = int(input('Favor informar o valor: '))
        continuar = input('Se você desejar parar digíte "0000" ').upper()
        Ntermos +=1
        x += y
        if continuar == "0000":
            break
    return f'a soma é {x}, sendo dígitados {Ntermos} termos'

print(calculo())