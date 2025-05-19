class Conta01:
    def __init__(self):
        self.cliente = "joao"
        self.agencia = "0001"
        self.NumerodaConta = "1010-2"
        self.saldo = 0 

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.  ")
        else:
            print("Valor inválido para depósito.")
    def sacar(self, valor):
        if valor < 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("Valor inválido para saque.")
# Criando o objeto da classe
conta = Conta01()

while True:
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para depositar: "))
        conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para sacar: "))
        conta.sacar(valor)
    elif opcao == "3":
        print(f"Encerrando... Saldo final: R${conta.saldo}")
        break
    else:
        print("Opção inválida. Tente novamente.")