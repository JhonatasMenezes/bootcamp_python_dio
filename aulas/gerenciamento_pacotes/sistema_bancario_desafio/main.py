from time import sleep
from pathlib import Path
from datetime import datetime
from objects.add_money import AddMoney
from objects.get_money import GetMoney
from objects.physical_person import PhysicalPerson
from objects.current_account import CurrentAccount
from objects.account import AccountIterator


ROOT_PATH = Path(__file__).parent

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


def transaction_log(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        date_now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        with open(ROOT_PATH / "log.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"[{date_now}] Função '{func.__name__.upper()}' executada com argumentos {args} e {kwargs}."
                f"Retornou {resultado}\n"
            )
        return resultado

    return wrapper


@transaction_log
def deposit(customers):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customers(cpf, customers)

    if not customer:
        print("\nCliente não encontrado!")
        return False

    value = float(input("Informe o valor do depósito: "))
    transaction = AddMoney(value)

    account = recover_customer_account(customer)
    if not account:
        return False

    customer.execute_transaction(account, transaction)
    return True


@transaction_log
def cash_out(customers):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customers(cpf, customers)

    if not customer:
        print("\nCliente não encontrado!")
        sleep(2)
        return False

    value = float(input("Informe o valor do saque: "))
    transaction = GetMoney(value)

    account = recover_customer_account(customer)
    if not account:
        return False

    customer.execute_transaction(account, transaction)
    return True


@transaction_log
def show_records(customers, transaction_type=None):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customers(cpf, customers)

    if not customer:
        print("\nCliente não encontrado!")
        sleep(2)
        return False

    account = recover_customer_account(customer)
    if not account:
        return False

    print("\n================ EXTRATO ================")
    extract = ""
    transaction_existis = False
    for transaction in account.records.generate_report():
        transaction_existis = True
        extract += f"\n{transaction['date_time']}\n{transaction['transaction_type']}:\n\tR$ {transaction['value']:.2f}"

    if not transaction_existis:
        extract = "Não foram realizadas movimentações."

    print(extract)
    print(f"\nSaldo:\n\tR$ {account.balance:.2f}")
    print("==========================================")
    sleep(5)
    return True


@transaction_log
def add_customer(customers):
    cpf = input("Informe o CPF (somente número): ")
    customer = filter_customers(cpf, customers)

    if customer:
        print("\nJá existe cliente com esse CPF!")
        sleep(2)
        return False

    name = input("Informe o nome completo: ")
    birth_date = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    customer = PhysicalPerson(
        name=name, birth_date=birth_date, cpf=cpf, address=address
    )

    customers.append(customer)

    print("\nCliente criado com sucesso!")
    sleep(2)
    return True


@transaction_log
def add_account(account_id, customers, accounts):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customers(cpf, customers)

    if not customer:
        print("\nCliente não encontrado, fluxo de criação de account encerrado!")
        sleep(2)
        return False

    account = CurrentAccount.new_account(account_id=account_id, customer=customer)
    accounts.append(account)
    customer.accounts.append(account)

    print("\nConta criada com sucesso!")
    sleep(2)
    return True


def list_accounts(accounts):
    for account in AccountIterator(accounts):
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
            print(
                "Operação inválida, por favor selecione novamente a operação desejada"
            )


main()
