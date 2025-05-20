# Exemplo de manipulação de arquivos CSV e JSON
import csv
import json

# Escrevendo e lendo CSV
with open('exemplo.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['nome', 'idade'])
    writer.writerow(['Ana', 25])
    writer.writerow(['João', 30])

with open('exemplo.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for linha in reader:
        print(linha)

# Escrevendo e lendo JSON
pessoa = {'nome': 'Ana', 'idade': 25}
with open('exemplo.json', 'w') as jsonfile:
    json.dump(pessoa, jsonfile)

with open('exemplo.json', 'r') as jsonfile:
    dados = json.load(jsonfile)
    print(dados)
