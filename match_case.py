numero = int(input("01 - INICIAR \n 02 - PAUSAR \n 03 - ENCERRAR\nDigite a opção desejada:\n "))

def menu(numero):
    match numero:
        case 1:
            print("Iniciado")
        case 2:
            print("Pausado")
        case 3:
            print("Encerrado")
        case _:
            print("ERRO")

menu(numero)
