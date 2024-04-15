from time import sleep
from datetime import datetime
from objects.add_money import AddMoney
from objects.get_money import GetMoney
from objects.physical_person import PhysicalPerson
from objects.current_account import CurrentAccount
from objects.records import Records

transaction_logs = []

def menu():
    menu = """\n
    ================ MENU ================
    [1] Depositar        Listar Contas [5]
    [2] Sacar            Novo Usuário  [6]
    [3] Extrato          Sair          [7]
    [4] Nova Conta
   
    => """
    return input(menu)

def filter_customers(cpf, customers):
    filtered_customers = [customer for customer in customers if customer.cpf == cpf]
    return filtered_customers[0] if filtered_customers else None


def recover_customer_account(customer):
    if not customer.accounts:
        print("\nCliente não possui conta!")
        sleep(2)
        return

    return customer.accounts[0]


def transaction_log(func,):
    def wrapper(*args, **kwargs):
        date_now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        try:
            func(*args, **kwargs)
            response = {"date_time": date_now, "transaction_type": func.__name__, "status": "success"}
        except Exception as exception:
            response = {"date_time": date_now, "transaction_type": func.__name__, "status": exception}

        transaction_logs.append(response)
    
    return wrapper


@transaction_log
def deposit(customers):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customers(cpf, customers)

    if not customer:
        print("\nCliente não encontrado!")
        return

    value = float(input("Informe o valor do depósito: "))
    transaction = AddMoney(value)

    account = recover_customer_account(customer)
    if not account:
        return

    customer.execute_transaction(account, transaction)


@transaction_log
def cash_out(customers):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customers(cpf, customers)

    if not customer:
        print("\nCliente não encontrado!")
        sleep(2)
        return

    value = float(input("Informe o valor do saque: "))
    transaction = GetMoney(value)

    account = recover_customer_account(customer)
    if not account:
        return

    customer.execute_transaction(account, transaction)


@transaction_log
def show_records(customers, transaction_type=None):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customers(cpf, customers)

    if not customer:
        print("\nCliente não encontrado!")
        sleep(2)
        return

    account = recover_customer_account(customer)
    if not account:
        return

    print("\n================ EXTRATO ================")
    transactions = account.records.transactions

    extract = ""
    if not transactions:
        extract = "Não foram realizadas movimentações."
    else:
        for transaction in transactions:
            extract += f"\n{transaction['transaction_type']}:\n\tR$ {transaction['value']:.2f}"

    print(extract)
    print(f"\nSaldo:\n\tR$ {account.balance:.2f}")
    print("==========================================")


@transaction_log
def add_customer(customers):
    cpf = input("Informe o CPF (somente número): ")
    customer = filter_customers(cpf, customers)

    if customer:
        print("\nJá existe cliente com esse CPF!")
        sleep(2)
        return

    name = input("Informe o nome completo: ")
    birth_date = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    customer = PhysicalPerson(name=name, birth_date=birth_date, cpf=cpf, address=address)

    customers.append(customer)

    print("\nCliente criado com sucesso!")
    sleep(2)


@transaction_log
def add_account(account_id, customers, accounts):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customers(cpf, customers)

    if not customer:
        print("\nCliente não encontrado, fluxo de criação de account encerrado!")
        sleep(2)
        return

    account = CurrentAccount.new_account(account_id=account_id, customer=customer)
    accounts.append(account)
    customer.accounts.append(account)

    print("\nConta criada com sucesso!")
    sleep(2)


def list_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(account)
    
    sleep(4)



def main():
    customers = []
    accounts = []

    while True:
        option = int(menu())

        if option == 1:
            deposit(customers)
        
        elif option == 2:
            cash_out(customers)
        
        elif option == 3:
            show_records(customers)
        
        elif option == 4:
            account_id = len(accounts) + 1
            add_account(account_id, customers, accounts)
        
        elif option == 5:
            list_accounts(accounts)
        
        elif option == 6:
            add_customer(customers)
        
        elif option == 7:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")


main()