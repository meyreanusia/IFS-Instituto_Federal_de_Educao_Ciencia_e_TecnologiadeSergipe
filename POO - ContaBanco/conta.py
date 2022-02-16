class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def saca(self, valor):
        self.saldo -= valor

    def extrato(self):
        print(f"numero: {self.numero} \nsaldo: {self.saldo}")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            return True


