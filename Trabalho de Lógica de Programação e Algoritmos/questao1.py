"""
QUESTÃO 1 de 4 – Conteúdos até Aula 3

Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de um app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra, conforme a listagem abaixo:
⦁ Se valor for menor que 2500 o desconto será de 0%;
⦁ Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
⦁ Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
⦁ Se valor for igual ou maior que 10000 o desconto será de 11%;

Elabore um programa em Python que:
⦁ Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome [EXIGÊNCIA DE CÓDIGO 1 de 6];
⦁ Deve-se implementar o input do valor unitário e da quantidade do produto [EXIGÊNCIA DE CÓDIGO 2 de 6];
⦁ Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
⦁ Deve-se implementar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 4 de 6];
⦁ Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];  
⦁ Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
⦁ Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
⦁ Deve-se apresentar na saída de console um pedido recebendo desconto (valor total sem desconto maior ou igual a 2500) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];  
"""

"""
QUESTÃO 1 de 4 – Conteúdos até Aula 3

Enunciado:
Imagina-se que você é um dos programadores responsáveis pela construção de um app de vendas para uma determinada
empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da
compra, conforme a listagem abaixo:
    ⦁ Se valor for menor que 2500 o desconto será de 0%;
    ⦁ Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
    ⦁ Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
    ⦁ Se valor for igual ou maior que 10000 o desconto será de 11%.

Requisitos:
    • Implemente uma mensagem de boas-vindas que contenha seu nome e sobrenome.
    • Leia o valor unitário e a quantidade do produto via input.
    • Calcule o desconto conforme as faixas informadas.
    • Mostre o valor total sem desconto e o valor total com desconto.
    • Utilize as estruturas if, elif e else.
    • Insira comentários relevantes no código.
    • Apresente na saída de console uma mensagem de boas-vindas com seu nome.
    • Apresente na saída de console um pedido informando se houve desconto (para valores totais >= 2500).
"""

# Nome do usuário
nome = 'Fabrício Rosa'
print(f'Bem-vindo a Loja do {nome}.')

# Leitura dos inputs para o valor unitário e quantidade do produto
valor_unitario = float(input('Digite o valor unitário do produto: '))
quantidade = int(input('Digite a quantidade do produto: '))

# Cálculo do valor total sem desconto
valor_total_sem_desconto = quantidade * valor_unitario

# Condições da taxa de desconto com base no valor total da compra
if valor_total_sem_desconto < 2500:
        desconto = 0
elif 2500 <= valor_total_sem_desconto < 6000:
        desconto = 0.04
elif 6000 <= valor_total_sem_desconto < 10000:
        desconto = 0.07
else:
        desconto = 0.11

# Cálculo do valor total com o desconto aplicado
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto)

# Mensagem informando se houve desconto ou não
if desconto > 0:
        print(f'Você recebeu um desconto de {desconto * 100:.2f}%.')
else:
        print('Você não recebeu desconto.')

# Mensagem dos valores totais com e sem desconto
print(f'O valor total SEM desconto é: R$ {valor_total_sem_desconto:.2f}')
print(f'O valor total COM desconto é: R$ {valor_total_com_desconto:.2f}')
