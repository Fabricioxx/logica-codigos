# Exercício 7
# Peça ao usuário uma palavra e diga se ela é um palíndromo (lê igual de trás para frente).

palavra = input('Digite uma palavra: ')
if palavra == palavra[::-1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')
