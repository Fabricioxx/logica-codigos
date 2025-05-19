# Exemplo 4: Listas e laços
notas = [7.5, 8.0, 6.5, 9.0]
soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
print(f'Média das notas: {media:.2f}')
