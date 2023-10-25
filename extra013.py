#Gerador de Senhas
#Solicite ao usuário o comprimento desejado da senha e gere uma senha aleatória desse tamanho.
import string
import random

def gerador(tamanho):
    caracteres = string.ascii_letters + string.digits
    senha = random.choices(caracteres, k=tamanho)
    return ''.join(senha)

tamanho = int(input('Favor informar o tamanho da senha:'))
print(gerador(tamanho))
