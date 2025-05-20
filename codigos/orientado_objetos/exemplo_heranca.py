# Exemplo de herança em orientação a objetos
class Animal:
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        print(f"{self.nome} faz um som.")

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome} late!")

c = Cachorro("Rex")
c.falar()
