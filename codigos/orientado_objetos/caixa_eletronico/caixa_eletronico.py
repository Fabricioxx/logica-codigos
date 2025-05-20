"""
Projeto: Caixa Eletrônico Orientado a Objetos
Este projeto simula um caixa eletrônico no terminal, permitindo criar uma conta bancária, depositar, sacar, consultar saldo e sair.
"""

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# --- Programa principal ---
print("Bem-vindo ao Caixa Eletrônico!")
nome = input("Digite o nome do titular da conta: ")
conta = ContaBancaria(nome)

while True:
    print("\nEscolha uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Consultar saldo")
    print("4. Sair")
    opcao = input(">> ")
    if opcao == "1":
        valor = float(input("Valor para depósito: "))
        conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Valor para saque: "))
        conta.sacar(valor)
    elif opcao == "3":
        conta.consultar_saldo()
    elif opcao == "4":
        print("Obrigado por usar o caixa eletrônico. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
