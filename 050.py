#Escreva um programa que leia uma frase, e mostre uma formatação adaptável de acordo com o tamanho da frase, coordenado por uma função

def formato(frase, arg = '*'):
    print(arg * 2 * len(frase))
    print(f'{frase.center(len(frase*2))}')
    print(arg * 2 * len(frase))

def texto():
    frase = input('Favor inserir tua frase: ')
    return frase


frase = texto()

formato(frase, arg='#')





