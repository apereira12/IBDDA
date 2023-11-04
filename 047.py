#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1


ValorSolicitado = int(input('Informe o valor que será retirado:'))
Notas = [50, 20, 10, 1]



def menorquantidade():
    sobra = ValorSolicitado
    for i in Notas:
        if sobra >= i:
            quantidade = sobra//i
            sobra=sobra%i
            print(f'Quantidade de notas {i} é: {quantidade}')

menorquantidade()
