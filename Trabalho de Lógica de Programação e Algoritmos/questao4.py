"""
Software de gerenciamento de livros.
"""

# Nome do usuário
nome = 'Fabrício Rosa'
print(f'Bem-vindo a Livraria do {nome}.\n')

# Lista vazia para armazenar os livros
lista_livro = []
# Variável global para o ID dos livros
id_global = 0

# Função para cadastrar um livro
def cadastrar_livro(id, nome_livro=None, autor_livro=None, editora_livro=None):
    # Se não for passado por parâmetro, pede via input
    if nome_livro is None:
        nome_livro = input('Digite o nome do livro: ')
    if autor_livro is None:
        autor_livro = input('Digite o autor do livro: ')
    if editora_livro is None:
        editora_livro = input('Digite a editora do livro: ')
    # Cria um dicionário com os dados do livro
    livro = {
        'id': id,
        'nome': nome_livro,
        'autor': autor_livro,
        'editora': editora_livro
    }
    # Adiciona o dicionário à lista de livros
    lista_livro.append(livro)
    print(f'Livro "{nome_livro}" cadastrado com sucesso!\n')

# Função para consultar livros
def consultar_livro():
    while True:
        print('Escolha uma opção:')
        print('1. Consultar Todos')
        print('2. Consultar por Id')
        print('3. Consultar por Autor')
        print('4. Retornar ao menu')
        opcao = input('>> ').strip()
        if opcao == '1':
            if not lista_livro:
                print('Nenhum livro cadastrado.\n')
            else:
                for livro in lista_livro:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                print()
        elif opcao == '2':
            try:
                id_consulta = int(input('Digite o ID do livro: '))
            except ValueError:
                print('ID inválido.\n')
                continue
            livro_encontrado = next((livro for livro in lista_livro if livro['id'] == id_consulta), None)
            if livro_encontrado:
                print(f"ID: {livro_encontrado['id']}, Nome: {livro_encontrado['nome']}, Autor: {livro_encontrado['autor']}, Editora: {livro_encontrado['editora']}\n")
            else:
                print('Livro não encontrado.\n')
        elif opcao == '3':
            autor_consulta = input('Digite o autor do livro: ')
            livros_encontrados = [livro for livro in lista_livro if livro['autor'].lower() == autor_consulta.lower()]
            if livros_encontrados:
                for livro in livros_encontrados:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                print()
            else:
                print('Nenhum livro encontrado desse autor.\n')
        elif opcao == '4':
            break
        else:
            print('Opção inválida. Tente novamente.\n')

# Função para remover um livro
def remover_livro():
    while True:
        try:
            id_remover = int(input('Digite o ID do livro a ser removido: '))
        except ValueError:
            print('ID inválido. Tente novamente.\n')
            continue
        livro_encontrado = next((livro for livro in lista_livro if livro['id'] == id_remover), None)
        if livro_encontrado:
            lista_livro.remove(livro_encontrado)
            print(f'Livro "{livro_encontrado["nome"]}" removido com sucesso!\n')
            break
        else:
            print('ID inválido. Tente novamente.\n')

# -------- (main) --------

while True:
    print('Escolha uma opção:')
    print('1. Cadastrar Livro')
    print('2. Consultar Livro')
    print('3. Remover Livro')
    print('4. Encerrar Programa')
    opcao = input('>> ').strip()
    if opcao == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        print('Encerrando o programa. Até logo!')
        break
    else:
        print('Opção inválida. Tente novamente.\n')
