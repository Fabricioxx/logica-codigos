"""
QUESTÃO 3 de 4 - Conteúdo até aula 05

Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
A copiadora opera da seguinte maneira:
⦁ Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
⦁ Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
⦁ Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos; 
⦁ Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 
⦁ Se número de páginas for menor que 20 retornar o número de página sem desconto;
⦁ Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%;
⦁ Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%;
⦁ Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%;
⦁ Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;
⦁ Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
⦁ Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;
⦁ Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;

O valor final da conta é calculado da seguinte maneira:
total = (servico * num_pagina) + extra

[Demais exigências do enunciado...]
"""


#função para escolher o serviço
def escolha_servico():
  
    servicos = {
        'DIG': 1.10,
        'ICO': 1.00,
        'IPB': 0.40,
        'FOT': 0.20
    }

    while True:
        print("\nEntre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        tipo = input(">>").strip().upper()
        if tipo in servicos:
            return tipo, servicos[tipo]
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente\n")

# função para calcular o número de páginas
def num_pagina():
   
    while True:
        try:
            num = int(input("Entre com o número de páginas: "))
            if num >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.\n")
                continue
            elif num <= 0:
                print("Número de páginas inválido. Tente novamente.\n")
                continue

            # Condição de desconto conforme a faixa
            if num < 20:
                desconto = 0
            elif 20 <= num < 200:
                desconto = 0.15
            elif 200 <= num < 2000:
                desconto = 0.20
            else:  # 2000 até 19999
                desconto = 0.25

            return num, desconto

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.\n")

# função para escolher o serviço extra
def servico_extra():
    
    print("\nDeseja adicionar algum serviço?")
    print("1 - Encadernação Simples - R$ 15.00")
    print("2 - Encadernação Capa Dura - R$ 40.00")
    print("0 - Não desejo mais nada")

    while True:
        opcao = input(">>").strip()

        # condições para o valor do serviço extra
        if opcao == '1':
            return 15.00
        elif opcao == '2':
            return 40.00
        elif opcao == '0':
            return 0.00
        else:
            print("Opção inválida. Tente novamente.")


# -------- (main) --------


nome = "Fabrício Rosa"
print(f"Bem-vindo a Copiadora do {nome}.\n")

# Chama as funções
servico, preco_unitario = escolha_servico()
num_paginas, desconto = num_pagina()
valor_extra = servico_extra()

# Cálculo do valor total
valor_servico_com_desconto = preco_unitario * num_paginas * (1 - desconto)
valor_total = valor_servico_com_desconto + valor_extra

# Saída do valor final
print(f"\nTotal: R$ {valor_total:.2f} (serviço: {preco_unitario:.2f} * {num_paginas}: {valor_servico_com_desconto:.2f} + extra: {valor_extra:.2f})")


