# Exercício 10
# Peça ao usuário uma frase e conte quantas vogais ela possui.

frase = input('Digite uma frase: ').lower()
vogais = 0
for letra in frase:
    if letra in 'aeiou':
        vogais += 1
print(f'A frase tem {vogais} vogais.')
