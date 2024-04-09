# Sistema Bancário V2
# Regras desafio:
# 0 - Todas as operações devem se tornar funções
# 1 - Função saque deve receber argumentos keyword only (colocando nome do parâmetro antes do argumento)
# 2 - Função depósito deve receber argumentos por posição (colocar argumentos diretos sem referenciar parâmetros)
# 3 - Função extrato deve receber argumentos por posição e nome. Exemplo: (saldo (posicional), extrato=extrato)
# 4 - Criar duas novas funções: Cadastrar usuário em uma lista e Cadastrar nova conta corrente para o usuário que não possuir
# 5 - Composição usuário: nome, data nasc, cpf (somente números e sem repetição entre usuários) e endereço (logradouro - numero - bairro - cidade/sigla estado).
# 6 - Composição conta: agência (0001), n° da conta (sequencial começando por 1) e usuario. Cada usuário pode ter várias contas, mas a conta só pode ter um dono (usuário)

import os
from datetime import datetime
import mensagens_sistema as sys
from time import sleep


######## Criação de funções e constantes necessárias ########
LIMITE_SAQUE_VALOR = 500
USUARIOS = []
CONTAS = []


def adicionar_usuario(nome: str, data_nascimento: str, CPF: int, endereco):
    global USUARIOS
    global CONTAS
   
    USUARIOS.append({
            "nome": nome,
            "data_nascimento":data_nascimento,
            "CPF": CPF,
            "endereço": {
                "logradouro": endereco["logradouro"],
                "numero": endereco["numero"],
                "bairro": endereco["bairro"],
                "cidade": endereco["cidade"],
                "estado": endereco["estado"]
            }
        })
    conta_gerada = CONTAS[-1]["num_conta"] + 1
    CONTAS.append({
        "agencia": '0001',
        "num_conta": conta_gerada,
        "CPF_usuario": None,
        "saldo": 0,
        "extrato": []
    })
    
    resposta = f''''Usuário {nome} - CPF: {CPF} cadastrado com sucesso!
Anote o numero de sua conta: {conta_gerada}'''
    return resposta


def adicionar_conta(CPF: int):
    
    num_conta = CONTAS[-1]["num_conta"] + 1
    nova_conta = {
        "agencia": '0001',
        "num_conta": num_conta,
        "CPF_usuario": None,
        "saldo": None,
        "extrato": []
    }
    CONTAS.append(nova_conta)

    resposta = {
        "CPF": CPF,
        "agencia": nova_conta["agencia"],
        "conta": num_conta
    }
    return resposta


def confirmar_cadastro(CPF: int):
    global CONTAS
    global USUARIOS

    for usuario in USUARIOS:
        if usuario["CPF"] == CPF:
            return True
    
    return False


def cadastro_conta(CPF: int):
    confirmacao = adicionar_conta(CPF)
    os.system('cls')
    print("Conta adicionada com sucesso!")
    for chave, valor in confirmacao.items():
        print(f"{chave}: {valor}")
        sleep(1)
    sleep(2)
    input('Pressione enter para voltar ao menu anterior!')
    os.system('cls')


def cadastro_usuario(CPF: int):
    cpf = CPF
    if confirmar_cadastro(cpf):
        sys.erros(6)
    else:
        print("Informe os dados a seguir!")
        sleep(1)
        nome = str(input("Nome: "))
        data_nascimento = str(input("Data de Nascimento: "))
        logradouro = str(input("Logradouro (rua/avenida): "))
        numero_casa = int(input("N°: "))
        bairro = str(input("Bairro: "))
        cidade = str(input("Cidade: "))
        estado = str(input("Sigla estado: "))
        endereço = {
            "logradouro": logradouro,
            "numero": numero_casa,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }
        resposta = adicionar_usuario(nome, data_nascimento, cpf, endereço)
        print(resposta)
        sleep(2)
        input('Pressione enter para voltar ao menu anterior!')
        os.system('cls')



def buscar_dados(tipo: str, CPF: int):
    global CONTAS
    global USUARIOS

    lista_contas = []
    if tipo == "conta":
        for conta in CONTAS:
            if conta["CPF"] == CPF:
                lista_contas.append(conta)
        
        return lista_contas
    
    elif tipo == "usuario":
        for usuario in USUARIOS:
            if usuario["CPF"] == CPF:
                return usuario


def confirmacao_login(numero_conta: int, CPF: str):
    global CONTAS

    if confirmar_cadastro(CPF):
        for conta in CONTAS:
            if conta["num_conta"] == numero_conta:
                return True
    else:
        return False


def login(cpf, numero_conta):
    if confirmacao_login(numero_conta, cpf):
        return True
    else:
        return False


def depositar(numero_conta: int, valor: float):
    global CONTAS

    if valor < 0:
        sys.erros(1)
        sleep(2)
    else:
        for conta in CONTAS:
            if conta["num_conta"] == numero_conta:
                conta["saldo"] += valor

                data = str(datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
                conta["extrato"].append({data: f"Depósito:     + R$ {valor:.2f}"})

                print(f'Novo saldo: {conta["saldo"]:.2f}')
                sleep(2)
                input('Pressione enter para voltar ao menu anterior!')
                os.system('cls')


def sacar(numero_conta=None, valor=0):
    global CONTAS

    for conta in CONTAS:
        if conta["num_conta"] == numero_conta:
            conta["saldo"] -= valor

            data = str(datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
            conta["extrato"].append({data: f"Saque:     - R$ {valor:.2f}"})

            print(f'Novo saldo: {conta["saldo"]:.2f}')
            sleep(2)
            input('Pressione enter para voltar ao menu anterior!')
            os.system('cls')


def limitar_saque(numero_conta):
    global CONTAS

    saques_efetuados = 0
    data_hoje = str(datetime.now().strftime('%d/%m/%Y'))
    
    for conta in CONTAS:
        if numero_conta == conta["num_conta"]:
            for operacao in conta["extrato"]:
                for key, value in operacao.items():
                    if key[:10] == data_hoje and value[:5] == "Saque":
                        saques_efetuados += 1
                        if saques_efetuados == 3:
                            return True

    return False


def consultar_saldo(numero_conta):
    global CONTAS

    for conta in CONTAS:
        if conta["num_conta"] == numero_conta:
            return conta["saldo"]


def consultar_extrato(numero_conta):
    global CONTAS

    for conta in CONTAS:
        if conta["num_conta"] == numero_conta:
            extrato = conta["extrato"]
            data_extrato = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            if conta["saldo"] > 0:
                str_saldo = f"R$ {conta["saldo"]:.2f}"
            else:
                str_saldo = f"R$ 0"
            mensagem_extrato = ('='*65) +'\n'
            mensagem_extrato += f'{"Data/Hora".ljust(25, ' ')}  |  {data_extrato.rjust(35, ' ')}\n'
            mensagem_extrato += f'{"Saldo Disponível".ljust(25, ' ')}  |  {str_saldo.rjust(35, ' ')}\n'

            for dado in extrato:
                for key, value in dado.items():
                    mensagem_extrato += f'{key.ljust(25, ' ')}  |  {value.rjust(35, ' ')}\n'

            mensagem_extrato += ('='*65) +'\n'
            os.system('cls')
            print(mensagem_extrato)
            sleep(2)
            input('Pressione enter para voltar ao menu anterior!')
            os.system('cls')



######## Execução do Programa ########
while True:
    os.system('cls')
    opcao_inicial = int(input(sys.menu(1)))

    if opcao_inicial == 0:
        sys.encerrando()
        break

    elif opcao_inicial == 1:
        try:
            os.system('cls')
            cpf = int(input("CPF: "))
            numero_conta = int(input("N° da conta: "))
        except:
            sys.erros(5)
            break

        while True:
            if login(cpf, numero_conta):
                os.system('cls')
                opcao_conta = int(input(sys.menu(2)))
                if opcao_conta == 0:
                    break
            
                elif opcao_conta == 1:
                    try:
                        valor = float(input('Digite o valor que deseja depositar: '))
                    except:
                        sys.erros(0)
                        sys.encerrando()
                        continue

                    depositar(numero_conta, valor)

                elif opcao_conta == 2:
                    if limitar_saque(numero_conta):
                        sys.erros(3)
                        continue
                    try:
                        valor = float(input('Digite o valor que deseja sacar: '))
                    except:
                        sys.erros(0)
                        continue

                    if valor < 0:
                        sys.erros(0)
                        continue

                    elif valor > LIMITE_SAQUE_VALOR:
                        sys.erros(1)
                        continue

                    elif valor > float(consultar_saldo(numero_conta)):
                        sys.erros(2)
                        continue

                    else:
                        sacar(numero_conta=numero_conta, valor=valor)
                        os.system('cls')

                elif opcao_conta == 3:
                    consultar_extrato(numero_conta)
            else:
                sys.erros(8)
                break

    elif opcao_inicial == 2:
        try:
            os.system('cls')
            cpf = int(input("CPF: "))
        except:
            sys.erros(0)

        cadastro_usuario(cpf)
    
    elif opcao_inicial == 3:
        try:
            cpf = int(input("CPF: "))
        except:
            sys.erros(0)
        
        if confirmar_cadastro(cpf):
            cadastro_conta(cpf)
        else:
            sys.erros(7)
