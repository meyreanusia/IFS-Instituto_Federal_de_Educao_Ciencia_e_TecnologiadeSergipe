from datetime import datetime
import os
import time
import random

diaDaSemana = datetime.today().isoweekday()
parar = ""
cliente = []
entrega = []

def escreva(msg):
    tam = len(msg) + 4
    print("*" * tam)
    print(f"  {msg}")
    print("*" * tam)


def calculo_conta(pedidos):
    pizza = 50
    os.system("cls")
    if diaDaSemana == 1: #Promoçao aplicada Segunda-feira.
        if quantidade > 1:

            x = (pizza * pedidos) - 15
            print("Parabéns, Você acaba de ganhar 30% de desconto!!")
            time.sleep(3)
            print("A promoção de 30% será atribuida a apenas 1 pedido.")
            time.sleep(3)
            print(f"O valor total a ser pago por {nome} é: R$ {x:.2f} ")

        else:
            print(
                f"Parabéns, Você acaba de ganhar 30% de desconto!! \n O valor total a ser pago por {nome} é: R$ {pizza - 15:.2f}")
            time.sleep(3)

        time.sleep(3)
        os.system("cls")
    else: #Valores dias comuns
        y = pizza * pedidos

        print(f"O valor total a ser pago por {nome} é: R$ {y:.2f}")
        time.sleep(2)
        os.system("cls")


def delivery(entrega):
    os.system("cls")
    random.shuffle(entrega)

    while entrega:
        print(f"A ordem de entrega será: {entrega}")
        time.sleep(3)
        x = entrega.pop()
        print(f"O pedido de {x} foi entregue!")
        time.sleep(1)
        print("Agradecemos a preferencia!!")
        time.sleep(3)
        os.system("cls")

    time.sleep(1)
    print("TODOS OS PEDIDOS  FORAM ENTREGUES.")
    time.sleep(3)
    os.system("cls")


while parar != "N":  # LOOPING PROMOÇÃO

    if diaDaSemana == 1:
        escreva("Seja bem-vindo(a) à Forneria Italiana!!")
        time.sleep(1)
        pedido = str(input("Você deseja fazer o pedido S/N ? ")).upper()
        time.sleep(1)
        os.system("cls")

        if pedido == "N":
            parar = pedido

        elif pedido == "S":

            nome = str(input(f"Por favor, digite o seu nome: ")).upper()
            quantidade = int(input(f"{nome}, digite a quantidade de pizza desejada: "))

            if quantidade <= 0:
                print("Por favor, Digite uma opção válida.")
            else:
                for i in range(quantidade):

                    print("=" * 40)
                    sabor = int(input(f"Escolha os sabores desejados:\n [1] Calabresa\n"
                                      f" [2] Frango com catupiry\n"
                                      f" [3] 4 Queijos \n"
                                      f" [4] Pepperoni \n"
                                      f" [5] Nordestina \n"))
                    os.system("cls")

                    if 0 < sabor < 6:
                        continue
                    else:
                        print("Escolha um sabor disponível no menu.")
                        time.sleep(2)
                        os.system("cls")

                        print("=" * 40)
                        sabor = int(input(f"Escolha os sabores desejados:\n [1] Calabresa\n"
                                          f" [2] Frango com catupiry\n"
                                          f" [3] 4 Queijos \n"
                                          f" [4] Pepperoni \n"
                                          f" [5] Nordestina \n"))
                        os.system("cls")
                        time.sleep(2)
                cliente.append(nome)
                calculo_conta(quantidade)

        elif pedido == "N":
            print("Volte sempre! ")
            time.sleep(3)

        else:
            print(" Por favor, digite uma opção válida.")
            time.sleep(1)

        os.system("cls")

        if len(cliente) == 3:  # ESVAZIA A FILA E ADD À PILHA DE ENTREGA
            while cliente:
                x = cliente.pop(0)
                entrega.append(x)
                print(f"Pedido de {x} foi separado para entrega!")
                time.sleep(3)
                os.system("cls")

            delivery(entrega)  # CHAMADA DA FUNÇÃO

    else:  # DIAS SEM PROMOÇÃO
        escreva("Seja bem-vindo(a) à Forneria Italiana!!")
        time.sleep(1)
        pedido = str(input("Você deseja fazer o pedido S/N ? ")).upper()
        time.sleep(1)
        os.system("cls")

        if pedido == "N":
            parar = pedido

        elif pedido == "S":
            nome = str(input(f"Por favor, digite o seu nome: "))
            quantidade = int(input(f"{nome}, digite a quantidade de pizza desejada: "))

            if quantidade <= 0:
                print("Por favor, Digite uma opção válida.")
            else:
                for i in range(quantidade):  # ESCOLHA DE SABOR
                    print("=" * 40)
                    sabor = int(input(f"Escolha os sabores desejados:\n [1] Calabresa\n"
                                      f" [2] Frango com catupiry\n"
                                      f" [3] 4 Queijos \n"
                                      f" [4] Pepperoni \n"
                                      f" [5] Nordestina \n"))
                    os.system("cls")
                    if 0 < sabor < 6:
                        continue

                    else:
                        print("Escolha um sabor disponível no menu.")
                        time.sleep(2)
                        os.system("cls")

                        print("=" * 40)
                        sabor = int(input(f"Escolha os sabores desejados:\n [1] Calabresa\n"
                                          f" [2] Frango com catupiry\n"
                                          f" [3] 4 Queijos \n"
                                          f" [4] Pepperoni \n"
                                          f" [5] Nordestina \n"))
                cliente.append(nome)
                calculo_conta(quantidade)
        elif pedido == "N".lower():
            print("Volte sempre!")
            time.sleep(4)
        else:
            print(" Por favor, digite uma opção válida.")
        os.system("cls")
        time.sleep(3)

        if len(cliente) == 3:  # ESVAZIA A FILA E ADD À PILHA DE ENTREGA
            while cliente:
                x = cliente.pop(0)
                entrega.append(x)
                print(f"Pedido de {x} foi separado para entrega!")
                time.sleep(3)
                os.system("cls")
            delivery(entrega)  # CHAMADA DA FUNÇÃO
if cliente:
    while cliente:
        x = cliente.pop(0)
        entrega.append(x)
        print(f"Pedido de {x} foi separado para entrega!")
        time.sleep(3)
        os.system("cls")
    time.sleep(3)
    (delivery(entrega))

print("programa encerrado!!")
print("Volte Sempre!!")
espera = input()
