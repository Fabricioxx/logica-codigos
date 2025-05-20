# Exemplo de dicionário em Python
# Criação, acesso, iteração e métodos úteis
pessoa = {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa.get('idade')}")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
pessoa['profissao'] = 'Engenheira'
print(f"Dicionário atualizado: {pessoa}")
