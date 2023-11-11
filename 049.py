#Crie um programa que tenha a função área(), que receba as dimensões de um muro retangular e mostra a área do terreno

def funcao():
    try:
        x = int(input('Favor informar a largura do muro: '))
        y = int(input('Favor informar a altura do muro: '))
        area =  x*y
        print (f'sua área é de {area} m²')
    except ValueError:
        print('Tem que colocar numero')

funcao()