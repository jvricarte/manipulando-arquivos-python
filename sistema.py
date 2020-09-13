import interface as intf
import arquivo as aq
from time import sleep

arq = 'cadastros.txt'

if not aq.arquivo_existe(arq):
    aq.criar_arquivo(arq)

while True:
    resp = intf.menu(['Cadastrar novo', 'Ver cadastros', 'Sair do sistema'])
    if resp == 1:
        intf.cabecalho('CADASTRAR NOVO')
        nome = str(input('Nome: '))
        idade = intf.leia_int('Idade: ')
        aq.cadastrar(arq, nome, idade)
    elif resp == 2:
        intf.cabecalho('PESSOAS CADASTRADAS')
        aq.ler_arquivo(arq)
    elif resp == 3:
        intf.cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Por favor, digite um uma das opções acima!\033[m')
    sleep(1)
