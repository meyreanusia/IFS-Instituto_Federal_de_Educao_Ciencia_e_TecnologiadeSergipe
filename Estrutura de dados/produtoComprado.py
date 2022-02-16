
class ProdutoComprado:
    pass
    
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
    
    def __str__(self) -> str:
        return str(self.produto) + " - " + self.quantidade

    def toString(self):
        print("produto: {0}\nquantidade: {1}".format(self.produto, self.quantidade))