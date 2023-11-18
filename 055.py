#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois, deve mostrar para cada palavra, suas vogais

palavras = ('Valor', 'Corinthians','Brasil', 'EUA', 'Alisson')
def TestaVogal(palavras):

    vogal = ['a', 'e', 'i', 'o', 'u']
    for i in palavras:
        vogalpalavra = []
        for x in i:

            if(x in vogal):
                vogalpalavra.append(x)
        print(f'as vogais em {i} são {vogalpalavra}')




TestaVogal(palavras)