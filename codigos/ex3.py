# Exercício 3
# Peça um número ao usuário e mostre a tabuada desse número de 1 a 10.

numero = int(input('Digite um número para ver a tabuada: '))
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')
