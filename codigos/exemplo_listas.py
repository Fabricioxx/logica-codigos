# Exemplo 4: Listas e laços
# Cria uma lista de notas
notas = [7.5, 8.0, 6.5, 9.0]
# Inicializa a variável soma com zero
soma = 0
# Percorre cada nota na lista e soma ao total
for nota in notas:
    soma += nota
# Calcula a média dividindo a soma pelo número de notas
media = soma / len(notas)
# Exibe a média formatada com 2 casas decimais
print(f'Média das notas: {media:.2f}')
