#Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

#Apenas os 3 primeiros mais assistidos
#Os últimos 2 mais assistidos
#A lista em ordem alfabética
#Em que posição está “O rei leão”


filmes = ("Avatar", "Vingadores", "De Férias da Família", "O Predador: Primeira Presa", "Samaritano", "Rei Leão", "Não! Não Olhe!", "Medieval", "Depois do Universo", "My Policeman", "O Desconhecido", "Noites Brutais", "Enola Holmes 2", "A Mulher Rei", "Sob a Pele", "Super Mario Bros: O Filme")

print(f'os 3 filmes mais asssitidos são: {filmes[:3]}')
print(f'os 2 filmes menos asssitidos são: {filmes[-2:]}')
print(f'O rei Leão é o {filmes.index("Rei Leão")+1}° filme mais assistido')
