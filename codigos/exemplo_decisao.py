# Exemplo 1: Estruturas de decisão
# Solicita ao usuário que digite um número e converte para inteiro
numero = int(input('Digite um número: '))
# Verifica se o número é par usando o operador de resto (%)
if numero % 2 == 0:
    print('O número é par.')  # Se o resto for 0, é par
else:
    print('O número é ímpar.')  # Se não, é ímpar
