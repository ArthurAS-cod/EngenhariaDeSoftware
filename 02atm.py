conta = Conta()

valor = int(input("Digite o valor para depositar: "))
conta.depositar(valor)

print(f"saldo Atual: R${conta.saldo}")