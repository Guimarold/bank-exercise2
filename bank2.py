class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso na conta de {self.cliente.nome}.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso na conta de {self.cliente.nome}.")
            else:
                print(f"Saldo insuficiente na conta de {self.cliente.nome} para realizar o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def extrato(self):
        print(f"Extrato bancário de {self.cliente.nome}:")
        print(f"CPF: {self.cliente.cpf}")
        print(f"Saldo disponível: R${self.saldo}")

# Exemplo de uso do sistema bancário
cliente1 = Cliente("João", "123.456.789-10")
conta1 = ContaBancaria(cliente1, 1000)

cliente2 = Cliente("Maria", "987.654.321-00")
conta2 = ContaBancaria(cliente2, 500)

conta1.deposito(500)
conta1.saque(200)
conta1.extrato()

conta2.saque(600)
conta2.extrato()
