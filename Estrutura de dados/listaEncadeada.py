class No:
    def __init__(self, conteudo, proximoNo=None):
        self.conteudo = conteudo
        self.proximoNo = proximoNo

    def __str__(self) -> str:
        return self.conteudo

    def toString(self):
        return "Conteúdo: " + self.conteudo

class ListaEncadeada:

    def __init__(self, referenciaEntrada=None):
        self.referenciaEntrada: No = referenciaEntrada

    
    def get(self, indice):
        self.indiceValido(indice)
        if self.indiceValido(indice):
            noAuxiliar = self.referenciaEntrada
            noRetorno = No(None)
            it = 0
            while it <= indice:
                noRetorno = noAuxiliar
                noAuxiliar = noAuxiliar.proximoNo
                it += 1
            return noRetorno
        return None

    def size(self):
        tamanhoLista = 0
        referenciaAux = self.referenciaEntrada

        while True:
            if referenciaAux != None:
                tamanhoLista += 1
                if referenciaAux.proximoNo != None:
                    referenciaAux = referenciaAux.proximoNo
                else:
                    break
            else:
                break
        return tamanhoLista

    def remove(self, indice):
        noPivo: No = self.get(indice)

        if indice == 0:
            self.referenciaEntrada = noPivo.proximoNo
            return noPivo.conteudo
        
        noAnterior: No = self.get(indice - 1)
        noAnterior.proximoNo = noPivo.proximoNo
        return noPivo.conteudo

    def add(self, conteudo):
        novoNo = No(conteudo)

        if self.isEmpty():
            self.referenciaEntrada = novoNo
            return
        
        noAuxiliar = self.referenciaEntrada
        it = 0

        while it < (self.size() - 1):
            noAuxiliar = noAuxiliar.proximoNo
            it += 1

        noAuxiliar.proximoNo = novoNo
   
    
    def isEmpty(self):
        if self.referenciaEntrada == None:
            return True
        else:
            return False
    
    def indiceValido(self, indice):
        if indice >= self.size():
            return False
        return True

    def toString(self):
        it = 1
        no = self.referenciaEntrada
        text = "Conteúdo ->> " + str(no)
        while it < self.size():
            text = text + " ->> "
            pxNo = self.referenciaEntrada.proximoNo
            text = text + pxNo
            it += 1

        return text

    def __str__(self) -> str:
        it = 1
        no = self.referenciaEntrada
        text = "Conteúdo ->> " + str(no)
        while it < self.size():
            text = text + " ->> "
            pxNo = self.referenciaEntrada.proximoNo
            text = text + pxNo
            it += 1

        return text

    
