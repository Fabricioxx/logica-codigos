# Exemplo simples de classe em Python
# Classe representa um objeto com atributos e métodos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Maria", 30)
p1.apresentar()
