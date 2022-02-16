from conta import Conta

conta = Conta('123-4', 'joao', 120.0, 1000.0)
print(conta.numero)
print(conta.titular)
print(conta.saldo)
print("______________________________________")
conta.deposita(50.0)
print("depositando...")
conta.extrato()
conta.saca(20.0)
print("______________________________________")
print("Saldo atal:")
conta.extrato()
