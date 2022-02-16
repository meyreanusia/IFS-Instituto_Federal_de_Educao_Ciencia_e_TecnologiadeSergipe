
class Produto:
    pass
    
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
    
    def __str__(self) -> str:
        return str(self.codigo) + " - " + self.nome + " - " + str(self.preco)

    def toString(self):
        print("Codigo: {0}\n Nome: {1}".format(self.codigo, self.nome))

    def __eq__(self, __o) -> bool:
        __a = Produto(__o.codigo, __o.nome, __o.preco)
        if self.codigo == __a.codigo:
            return True
        else:
            return False

    def __great__(self, __o) -> bool:
        __o = Produto(__o.codigo, __o.nome, __o.preco)
        if self.codigo > __o.codigo:
            return True
        else:
            return False