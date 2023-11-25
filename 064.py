#Crie um programa onde o usuário possa digitar sete letras, e cadastre em uma única lista, que mantenha separado as consoantes das vogais

def teste():
    listaA = []
    vogais = []
    cons = []
    while len(listaA) < 7:
        letras = input('Favor informar uma letra')
        listaA.append(letras)
    for i in listaA:
        if i in 'aeiou':
           vogais.append(i)
        else:
            cons.append(i)
    print(f'Essas são as consoantes{cons} e essas são as {vogais} ')

teste()