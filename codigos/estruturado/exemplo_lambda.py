# Exemplo de função lambda em Python
# Funções anônimas e uso com map/filter
quadrado = lambda x: x * x
print(f"Quadrado de 5: {quadrado(5)}")
lista = [1, 2, 3, 4]
quadrados = list(map(lambda x: x**2, lista))
print(f"Quadrados: {quadrados}")
pares = list(filter(lambda x: x % 2 == 0, lista))
print(f"Pares: {pares}")
