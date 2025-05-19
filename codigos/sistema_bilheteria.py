# Sistema de Bilheteria de Cinema (Terminal)
# Este sistema simula a compra de ingressos para o cinema usando o terminal

def exibir_menu():
    # Função que mostra o menu de opções
    print('--- Sistema de Bilheteria ---')
    print('1. Ver filmes disponíveis')
    print('2. Comprar ingresso')
    print('3. Sair')

# Lista de filmes disponíveis, cada um é um dicionário com id, nome e preço
filmes = [
    {'id': 1, 'nome': 'Vingadores', 'preco': 20.0},
    {'id': 2, 'nome': 'Matrix', 'preco': 18.5},
    {'id': 3, 'nome': 'Toy Story', 'preco': 15.0}
]

# Lista para registrar os ingressos vendidos
ingressos_vendidos = []

# Loop principal do sistema
while True:
    exibir_menu()  # Mostra o menu
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        # Mostra os filmes disponíveis
        print('\nFilmes disponíveis:')
        for filme in filmes:
            print(f"{filme['id']}. {filme['nome']} - R$ {filme['preco']:.2f}")
        print()
    elif opcao == '2':
        # Compra de ingresso
        id_filme = int(input('Digite o ID do filme: '))
        # Procura o filme pelo ID
        filme_escolhido = next((f for f in filmes if f['id'] == id_filme), None)
        if filme_escolhido:
            nome_cliente = input('Seu nome: ')
            # Registra o ingresso vendido
            ingressos_vendidos.append({'cliente': nome_cliente, 'filme': filme_escolhido['nome']})
            print(f"Ingresso comprado para {filme_escolhido['nome']}! Obrigado, {nome_cliente}.\n")
        else:
            print('Filme não encontrado.\n')
    elif opcao == '3':
        # Sai do sistema
        print('Saindo do sistema. Até logo!')
        break
    else:
        # Opção inválida
        print('Opção inválida. Tente novamente.\n')
