# Exercício 5
# Peça ao usuário 5 números e mostre a média deles.

soma = 0
for i in range(5):
    numero = float(input(f'Digite o {i+1}º número: '))
    soma += numero
media = soma / 5
print(f'A média dos números é {media}')
