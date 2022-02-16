from produto import Produto
class ArvoreBinaria:
    def __init__(self, valor: Produto):
        self.esquerda = None
        self.direita = None
        self.valor = valor
        self.tam = 0

    def inserir(self, valor: Produto):
        if self.valor:
            self.tam += 1
            if not valor.__great__(self.valor):
                if self.esquerda is None:
                    self.esquerda = ArvoreBinaria(valor)
                else:
                    self.esquerda.inserir(valor)
            elif valor.__great__(self.valor):
                if self.direita is None:
                    self.direita = ArvoreBinaria(valor)
                else:
                    self.direita.inserir(valor)
            else:
                self.valor = valor

    def buscar(self, valor):
        codigo = valor
        valor = Produto(codigo, None, None)
        if self.valor.codigo:
            if not valor.__great__(self.valor):
                if self.esquerda is None:
                    return False
                else:
                    if valor.__eq__(self.esquerda.valor):
                        return self.esquerda.valor
                    else:
                        return self.esquerda.buscar(valor.codigo)
            elif valor.__great__(self.valor):
                if self.direita is None:
                    return False
                else:
                    if valor.__eq__(self.direita.valor):
                        return self.direita.valor
                    else:
                        return self.direita.buscar(valor.codigo)
            elif valor.__eq__(self.valor):
                return self.valor