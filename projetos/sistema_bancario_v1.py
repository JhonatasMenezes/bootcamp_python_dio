import os
from datetime import datetime
from time import sleep

MENU = """        Sistema Pycoin
==============================
Escolha a operação desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[0] SAIR
==============================
=>"""
MENSAGEM_ERRO_VALOR = """==============================
ERRO NA EXECUÇÃO!
MOTIVO: VALOR INVÁLIDO!
==============================
"""
MENSAGEM_ERRO_SAQUE_VALOR = """==============================
ERRO NA EXECUÇÃO!
MOTIVO: VALOR MAIOR QUE O PERMITIDO: R$ 500.00!
==============================
"""
MENSAGEM_ERRO_SALDO_INSUFICIENTE = """==============================
ERRO NA EXECUÇÃO!
MOTIVO: SALDO INSUFICIENTE!
==============================
"""
MENSAGEM_ERRO_SAQUES = """==============================
ERRO NA EXECUÇÃO!
MOTIVO: LIMITE DE SAQUES DIÁRIOS ATINGIDO!
==============================
"""

LIMITE_SAQUE_VALOR = 500
LIMITE_SAQUES = 3

saldo = 800
saques_efetuados = 0
extrato = {}

while True:

    os.system('cls')
    opcao = int(input(MENU))

    if opcao == 0:
        print('Encerrando execução', end='', flush=True)
        for i in range(10):
            sleep(0.2)
            print('.', end='', flush=True)
    
        os.system('cls')
        print('Execução encerrada!')
        sleep(1)
        break
    
    elif opcao == 1:
        try:
            valor = float(input('Digite o valor que deseja depositar: '))
        except:
            print(MENSAGEM_ERRO_VALOR)
            sleep(2)
            input('Pressione enter para voltar ao menu inicial!')
            os.system('cls')
            continue

        if valor < 0:
            print(MENSAGEM_ERRO_VALOR)
            sleep(2)
            continue
        else:
            saldo += float(valor)

            extrato[datetime.now().strftime('%d/%m/%Y - %H:%M:%S')] = f"Depósito:     + R$ {valor:.2f}"

            print(f'Novo saldo: {saldo:.2f}')
            sleep(2)
            input('Pressione enter para voltar ao menu inicial!')
            os.system('cls')
    
    elif opcao == 2:
        if saques_efetuados == LIMITE_SAQUES:
            print(MENSAGEM_ERRO_SAQUES)
            sleep(2)
            input('Pressione enter para voltar ao menu inicial!')
            os.system('cls')
            continue
        try:
            valor = float(input('Digite o valor que deseja sacar: '))
        except:
            print(MENSAGEM_ERRO_VALOR)
            sleep(2)
            input('Pressione enter para voltar ao menu inicial!')
            os.system('cls')
            continue

        if valor < 0:
            print(MENSAGEM_ERRO_VALOR)
            sleep(2)
            input('Pressione enter para voltar ao menu inicial!')
            os.system('cls')
            continue
        elif valor > LIMITE_SAQUE_VALOR:
            print(MENSAGEM_ERRO_SAQUE_VALOR)
            sleep(2)
            input('Pressione enter para voltar ao menu inicial!')
            os.system('cls')
            continue
        elif valor > saldo:
            print(MENSAGEM_ERRO_SALDO_INSUFICIENTE)
            sleep(2)
            input('Pressione enter para voltar ao menu inicial!')
            os.system('cls')
            continue
        else:
            saldo -= float(valor)
            saques_efetuados += 1

            extrato[datetime.now().strftime('%d/%m/%Y - %H:%M:%S')] = f"Saque:        - R$ {valor:.2f}"

            print(f'Novo saldo: {saldo:.2f}')
            sleep(2)
            input('Pressione enter para voltar ao menu inicial!')
            os.system('cls')

    elif opcao == 3:
        data_extrato = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        str_saldo = f"R$ {saldo:.2f}"
        mensagem_extrato = ('='*65) +'\n'
        mensagem_extrato += f'{"Data/Hora".ljust(25, ' ')}  |  {data_extrato.rjust(35, ' ')}\n'
        mensagem_extrato += f'{"Saldo Disponível".ljust(25, ' ')}  |  {str_saldo.rjust(35, ' ')}\n'

        for key, value in extrato.items():
            mensagem_extrato += f'{key.ljust(25, ' ')}  |  {value.rjust(35, ' ')}\n'

        mensagem_extrato += ('='*65) +'\n'
        os.system('cls')
        print(mensagem_extrato)
        sleep(2)
        input('Pressione enter para voltar ao menu inicial!')
        os.system('cls')

