# Exercício 1
# Escreva um programa que peça ao usuário um número e mostre se ele é positivo, negativo ou zero.

numero = int(input('Digite um número: '))
if numero > 0:
    print('O número é positivo.')
elif numero < 0:
    print('O número é negativo.')
else:
    print('O número é zero.')
