import os
from time import sleep


def erros(erro: int) -> str:
    erros = [
        "VALOR INVÁLIDO", 
        "VALOR MAIOR QUE O PERMITIDO: R$ 500.00", 
        "SALDO INSUFICIENTE", 
        "LIMITE DE SAQUES DIÁRIOS ATINGIDO",
        "USUÁRIO INVÁLIDO",
        "USUÁRIO OU CONTA INVÁLIDA",
        "USUÁRIO JÁ CADASTRADO",
        "USUÁRIO NÃO ENCONTRADO",
        "ERRO DESCONHECIDO"
    ]
    erro_msg = erros[erro]
    resposta = f"""==============================
ERRO NA EXECUÇÃO!
MOTIVO: {erro_msg}!
==============================
"""
    os.system('cls')
    print(resposta)
    sleep(1)
    input('Pressione enter para voltar ao menu anterior!')
    os.system('cls')

def menu(opcao: int):
    menu_inicial = """        Sistema Pycoin
==============================
Escolha a operação desejada:

[1] Acessar
[2] Novo Usuário
[3] Nova Conta
[0] SAIR
==============================
=>"""


    menu_conta = """        Sistema Pycoin
==============================
Escolha a operação desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Voltar ao menu principal
==============================
=>"""

    if opcao == 1:

        return menu_inicial
    elif opcao == 2:
        return menu_conta

def voltar_menu():
    sleep(2)
    input('Pressione enter para voltar ao menu anterior!')
    os.system('cls')

def encerrando():
    print('Encerrando execução', end='', flush=True)
    for i in range(10):
        sleep(0.2)
        print('.', end='', flush=True)

    os.system('cls')
    print('Execução encerrada!')
    sleep(1)

