#Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso


extenso = ('um','dois','três','quatro', 'cinco', 'seis','sete', 'oito','nove','dez','onze','doze','treze','quatorze','quinze')

numero = int(input('Favor informar o número de 1 a 15: ')) - 1

numeroporextenso = extenso[numero]

print(numeroporextenso)