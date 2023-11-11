#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

'''Qual é o total gasto na compra
Quantos produtos custam mais de R$1000,00
Qual é o produto mais barato'''



def programa():
   dicio = {}
   produto = input('Favor informar o item: ')
   valor = float(input('Favor informar o valor do item: '))
   dicio[produto] = valor

   while True:
       escolha = input('Você deseja continuar? s/n: ').upper()
       if escolha == "N":
            print('Você finalizou sua lista')
            break
       produto = input('Favor informar o item: ')
       valor = float(input('Favor informar o valor do item: '))
       dicio[produto] = valor
   return dicio

dicio = programa()

def testes(dicio):
    print("****** Sua lista ******")
    c = 0
    for i in dicio.keys():
        c +=1
        print(f'Item {c}: {i} e Valor: R${dicio[i]:.2f}')

    maisBarato = float('inf')
    Produto = ""
    soma = 0
    qtd = 0

    #iterar sobre as chaves do dicionario
    for i in dicio.keys():
        soma += dicio[i]
        if dicio[i] >= 1000:
            qtd += 1
        if dicio[i] < maisBarato:
            maisBarato = dicio[i]
            Produto = i
    print(f'a soma dos produtos é de R${soma:.2f} e temos {qtd} de produtos acima de R$1000 e o produto mais barato é {Produto} e ele custa R${maisBarato:.2f}')


programa()
testes(dicio)




