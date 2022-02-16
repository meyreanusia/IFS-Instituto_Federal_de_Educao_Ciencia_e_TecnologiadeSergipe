import os, time
from listaEncadeada import ListaEncadeada
from produto import Produto
from estoqueProdutos import ArvoreBinaria
from produtoComprado import ProdutoComprado


listadeCompra = ListaEncadeada()
estoqueProdutos = ArvoreBinaria(Produto(100, None, None))
estoqueProdutos.inserir(Produto(200, "Feijão", 8.50))
estoqueProdutos.inserir(Produto(300, "Arroz", 6.50))


def inicio():
    os.system("cls")
    print("============== Mercearia Dois Irmãos ============== \n")
    opc = input("[1] Sistema de Caixa \n[2] Sistema de Estoque\n>>> ")
    if opc == "1":
        menuCaixa()
    elif opc == "2":
        menuEstoque()
    else:
        print("Opção inválida!")
        time.sleep(2)
        inicio()


def menuEstoque():
    os.system("cls")
    print("Menu Estoque\n")
    opc = input("[1] Registrar Produto \n[0] Voltar para o Início\n>>> ")
    if opc == "1":
        registrarProduto()
    elif opc == "0":
        inicio()
    else:
        print("Opção inválida!")
        time.sleep(2)
        menuEstoque()


def menuCaixa():
    os.system("cls")
    print("Sistema de Caixa\n")
    opc = input("[1] Iniciar novo Atendimento \n[0] Voltar para o Início\n>>> ")
    if opc == "1":
        menuAtendimento()
    elif opc == "0":
        inicio()
    else:
        print("Opção inválida!")
        time.sleep(2)
        menuCaixa()


def registrarProduto(): #CADASTRA PRODUTOS DA ARVORE
    os.system("cls")
    print("=== Registrar Produto ===")
    codigo = int(input("Código do Produto: "))
    nome = input("Nome do Produto: ")
    preco = float(input("Preço do Produto: "))
    produto = Produto(codigo, nome, preco)
    salvarNaArvore(produto)
    inicio()


def salvarNaArvore(produto): #ADICIONA OS PRODUTOS À ARVORE
    print(produto)
    estoqueProdutos.inserir(produto)
    time.sleep(3)


def menuAtendimento(): #ATENDIMENTO CAIXA
    os.system("cls")

    print("Atendimento Caixa")
    codigo = int(input("Digite o Código do Produto: "))
    produto = estoqueProdutos.buscar(codigo)

    if produto:
        quantidade = int(input("Digite a quantidade do Produto: "))
        produtoComprado = ProdutoComprado(produto, quantidade)

        listadeCompra.add(produtoComprado) # ADICIONAR À LISTA ENCADEADA
        imprimirLista()
    else:
        print("Produto não cadastrado no sistema!")
    time.sleep(3)


    opc = input(f"\nEscolha uma opção: \n[1] Passar um novo produto \n[2] Cancelar produto da lista de compra \n ")
    if opc == "1":
        time.sleep(2)
        menuAtendimento()
    else:

        indice = int(input("Digite o índice do produto a ser excluído: "))

        listadeCompra.remove(indice - 1) #REMOVE DA LISTA ENCADEADA
        imprimirLista()
        time.sleep(2)
        menuAtendimento()


def imprimirLista():
    tam = listadeCompra.size()
    indice = 0
    valortotal = 0
    while tam > 0:
        produtoComprado = listadeCompra.get(indice).conteudo
        indice += 1
        print(
            f'Índice: {str(indice)} ' + f'Produto: {produtoComprado.produto.nome} ' + f'Valor: R${str(produtoComprado.quantidade * produtoComprado.produto.preco)}')
        x = float(produtoComprado.quantidade * produtoComprado.produto.preco)
        tam -= 1
        valortotal = x + valortotal

    print(f"Valor total: R${valortotal}")



inicio()
