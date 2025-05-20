# Exercício 2
# Peça dois números ao usuário e mostre o maior deles.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print(f'O maior número é {num1}')
elif num2 > num1:
    print(f'O maior número é {num2}')
else:
    print('Os dois números são iguais.')
