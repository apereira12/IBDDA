#Escreva um programa que crie uma lista com os números de 1 a 10 e, em seguida, exiba apenas os números ímpares da lista.
import random


def numeros():
   lista = list(range(1,11))
   for i in lista:
       if i % 2 != 0:
           print(i)

numeros()