#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela, com a formatação correta


def matriz():
    m1 = []
    m2 = []
    m3 = []
    try:
        while len(m3)<3:
            m1_valor = float(input('Favor informar o valor da 1° matriz'))
            m1.append(m1_valor)
            m2_valor = float(input('Favor informar o valor da 2° matriz'))
            m2.append(m2_valor)
            m3_valor = float(input('Favor informar o valor da 3° matriz'))
            m3.append(m3_valor)
    except ValueError:
        print('Favor imprimir apenas números')

    matriz = [m1,m2,m3]

    for i in matriz:
        for x in i:
            print(x, end=' ')
        print()



matriz()