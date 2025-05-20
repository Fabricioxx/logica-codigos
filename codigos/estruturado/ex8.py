# Exercício 8
# Crie um programa que leia 10 números e mostre quantos são pares e quantos são ímpares.

pares = 0
impares = 0
for i in range(10):
    numero = int(input(f'Digite o {i+1}º número: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Pares: {pares}, Ímpares: {impares}')
