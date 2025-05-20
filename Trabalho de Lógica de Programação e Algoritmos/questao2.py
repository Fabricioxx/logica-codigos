"""
QUESTÃO 2 de 4 - Conteúdo até aula 04

Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:
⦁ Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
⦁ Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
⦁ Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;

Elabore um programa em Python que: 
⦁ Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome [EXIGÊNCIA DE CÓDIGO 1 de 8];
⦁ Deve-se implementar o input do sabor (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de CP e AC [EXIGÊNCIA DE CÓDIGO 2 de 8];
⦁ Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
⦁ Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];
⦁ Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];
⦁ Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
⦁ Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
⦁ Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
⦁ Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
⦁ Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
⦁ Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
⦁ Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];  
"""

# Nome do usuário
nome = 'Fabrício Rosa'
print(f'Bem-vindo a Loja do {nome}.')

# Exibe o cardápio com os preços
print('\n------ CARDÁPIO ------')
print('Tamanho | Cupuaçu (CP) | Açaí (AC)')
print('   P    |   R$ 9,00    |  R$ 11,00')
print('   M    |   R$ 14,00   |  R$ 16,00')
print('   G    |   R$ 18,00   |  R$ 20,00')
print('-----------------------\n')


acumulador = 0
# Loop para múltiplos pedidos
while True:
    # Leitura do sabor
    sabor = input('Digite o sabor (CP para Cupuaçu ou AC para Açaí): ').strip().upper()
    if sabor not in ['CP', 'AC']:
        print('Sabor inválido. Tente novamente.\n')
        continue  # Volta ao início do loop se o sabor for inválido

    # Leitura do tamanho
    tamanho = input('Digite o tamanho (P, M ou G): ').strip().upper()
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente.\n')
        continue  # Volta ao início do loop se o tamanho for inválido

    # Condição de preço com base no sabor e tamanho
    if sabor == 'CP':
        nome_sabor = 'Cupuaçu'
        if tamanho == 'P':
            preco = 9
        elif tamanho == 'M':
            preco = 14
        else:  # tamanho == 'G'
            preco = 18
    else:  # sabor == 'AC'
        nome_sabor = 'Açaí'
        if tamanho == 'P':
            preco = 11
        elif tamanho == 'M':
            preco = 16
        else:  # tamanho == 'G'
            preco = 20

    # Mostra o pedido feito pelo usuário
    print(f'Você pediu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}\n')

    # Adiciona o preço ao acumulador
    acumulador += preco

    # Pergunta se deseja fazer mais um pedido
    mais_um_pedido = input('Deseja pedir mais alguma coisa? (s/n): ').strip().lower()
    if mais_um_pedido != 's':
        break  # Sai do loop se a resposta não for 's'
# Exibe o total acumulado
print(f'Valor total a ser pago: R$ {acumulador:.2f}\n')

print('Obrigado por fazer seu pedido!')
