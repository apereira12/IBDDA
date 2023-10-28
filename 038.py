#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
'''
1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa'''

print('CALCULADORA PYTHON')
print('\n soma = 1','\n multiplicação = 2', '\n Maior = 3', '\n Novos números = 4 \n Sair do programa = 5')

def arg():
    opcao = int(input('Favor escolha um número da opcao: '))
    arg1 = int(input('Favor escolha o  1num da operação: '))
    arg2 = int(input('Favor escolha o  2num da operação: '))
    arg3 = int(input('Favor escolha o  3num da operação: '))

    return opcao,arg1,arg2,arg3

def calcuadora(a, x, y, z):
    while a != 5:
        if a == 1:
            resultado = x + y + z

        elif a == 2:
            resultado = x * y * z

        elif a == 3:
            resultado = max(x,y,z)

        elif a == 4:
            return
        else:
            print("Opção inválida. Por favor, escolha uma operação entre 1 e 4.")
            return

        a = int(input('Escolha um número da opção: '))
        print(resultado)


opcao,x,y,z = arg()
calcuadora(opcao,x,y,z)
