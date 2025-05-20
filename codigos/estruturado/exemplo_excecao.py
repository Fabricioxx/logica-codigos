# Exemplo de tratamento de exceções detalhado
try:
    numero = int(input('Digite um número inteiro: '))
    resultado = 10 / numero
except ValueError:
    print('Você não digitou um número inteiro!')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
else:
    print(f'Resultado: {resultado}')
finally:
    print('Fim do exemplo de exceção.')
