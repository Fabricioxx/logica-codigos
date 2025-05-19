# Exercício 6
# Peça um número ao usuário e mostre se ele é primo.

numero = int(input('Digite um número: '))
eh_primo = True
if numero < 2:
    eh_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
if eh_primo:
    print('O número é primo.')
else:
    print('O número não é primo.')
