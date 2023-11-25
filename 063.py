#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
#se a expressão passada está com os parênteses abertos e fechados na ordem correta

def listas():
    qParentesesDireita = 0
    qParentesesEsquerda = 0
    valor = input('Favor inserir sua expressão: ')
    posicaoD = []
    posicaoE = []

    for i in range(len(valor)):
        if valor[i] == ")":
            qParentesesDireita += 1
            posicaoD.append(i+1)

        elif valor[i] == "(":
            qParentesesEsquerda+=1
            posicaoE.append(i+1)




    print(posicaoD)
    print(posicaoE)
    print(f'{qParentesesDireita} e {qParentesesEsquerda}')




listas()