# Exemplo de manipulação de arquivos em Python
# Escrevendo e lendo um arquivo texto
with open('exemplo_arquivo.txt', 'w') as arquivo:
    arquivo.write('Olá, este é um exemplo de escrita em arquivo!')

with open('exemplo_arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(f"Conteúdo do arquivo: {conteudo}")
