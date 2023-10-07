
import random
opcoes = ('pedra','papel','tesoura')
escolhamaquina = random.choice(opcoes)
suaescolha = input('Escolha pedra, papel, tesoura: ').lower()

dicionario = {
    'pedra': {'pedra': 'empate', 'papel': 'você vence', 'tesoura': 'máquina vence'},
    'papel': {'pedra': 'máquina vence', 'papel': 'empate', 'tesoura': 'você vence'},
    'tesoura': {'pedra': 'você vence', 'papel': 'máquina vence', 'tesoura': 'empate'}
}

def jokenpo():
    if suaescolha in dicionario:
        return dicionario[escolhamaquina][suaescolha]
    else:
        return 'Opção inválida'

print(jokenpo())