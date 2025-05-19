# Sistema de Bilheteria de Cinema (Terminal)

def exibir_menu():
    print('--- Sistema de Bilheteria ---')
    print('1. Ver filmes disponíveis')
    print('2. Comprar ingresso')
    print('3. Sair')

filmes = [
    {'id': 1, 'nome': 'Vingadores', 'preco': 20.0},
    {'id': 2, 'nome': 'Matrix', 'preco': 18.5},
    {'id': 3, 'nome': 'Toy Story', 'preco': 15.0}
]

ingressos_vendidos = []

while True:
    exibir_menu()
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        print('\nFilmes disponíveis:')
        for filme in filmes:
            print(f"{filme['id']}. {filme['nome']} - R$ {filme['preco']:.2f}")
        print()
    elif opcao == '2':
        id_filme = int(input('Digite o ID do filme: '))
        filme_escolhido = next((f for f in filmes if f['id'] == id_filme), None)
        if filme_escolhido:
            nome_cliente = input('Seu nome: ')
            ingressos_vendidos.append({'cliente': nome_cliente, 'filme': filme_escolhido['nome']})
            print(f"Ingresso comprado para {filme_escolhido['nome']}! Obrigado, {nome_cliente}.\n")
        else:
            print('Filme não encontrado.\n')
    elif opcao == '3':
        print('Saindo do sistema. Até logo!')
        break
    else:
        print('Opção inválida. Tente novamente.\n')
