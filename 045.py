#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000




numero = None

while numero !=0000:
    numero = int(input('Insira o número que você quer saber a tabuada:'))
    for i in range(1, 11):
        print(f'|{numero}   x    {i} = {numero * i} |')




