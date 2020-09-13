def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leia_int('Sua opção: ')
    return opc


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferio não digitar o número.\033[m')
            return 0
        else:
            return n


