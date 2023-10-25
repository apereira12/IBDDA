#Calculadora de Gorjeta
#Solicite ao usuário o valor da conta e a porcentagem da gorjeta que eles gostariam de dar, em seguida, calcule o valor total da conta incluindo a gorjeta.
def gorjeta(valorconta,porcentagem):
    valorgorjeta=valorconta*(porcentagem/100)
    valortotal=valorgorjeta+valorconta
    print(f'O valor da sua conta é de R${valorconta:.2f}'
          f'\n você optou por dar {porcentagem}% de gorjeta totalizando R${valorgorjeta:.2f} de gorjeta,'
          f'\n logo sua conta ficará em R${valortotal:.2f}')


valorconta = float(input('Favor informar o valor da sua conta(R$): '))
porcentagem = float(input('Favor informar a porcentagem que você quer dar de gorjeta em %: '))

gorjeta(valorconta,porcentagem)
