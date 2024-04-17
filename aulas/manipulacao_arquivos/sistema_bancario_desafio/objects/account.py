from time import sleep
from typing import List
from.account_interface import AccountInterface
from .customer import Customer
from .records import Records

class Account(AccountInterface):
    def __init__(self, account_id: int, customer: Customer) -> None:
        self.__account_id = account_id
        self.__agency = "0001"
        self.__balance = 0
        self.__customer = customer
        self.__records = Records()


    @property
    def account_id(self) -> int:
        return self.__account_id
    
    
    @property
    def balance(self) -> float:
        return self.__balance
   
   
    @property
    def agency(self) -> str:
        return self.__agency
    
    
    @property
    def customer(self) -> Customer:
        return self.__customer
    
    
    @property
    def records(self) -> List:
        return self.__records


    @classmethod
    def new_account(cls, account_id: int, customer: Customer):
        return cls(account_id, customer)


    def cash_out(self, value: float) -> bool:
        balance = self.balance
        passed_balance = value > balance

        if passed_balance:
            print("\nFalha na operação! Saldo insuficiente.")
            sleep(2)

        elif value > 0:
            self.__balance -= value
            print("\nSaque realizado com sucesso!")
            sleep(2)
            return True

        else:
            print("\nFalha na operação! Valor inválido")
            sleep(2)

        return False
    

    def deposit(self, value: float) -> bool:
        if value > 0:
            self.__balance += value
            print("\nDepósito realizado com sucesso!")
            sleep(2)
            return True
        
        else:
            print("\nFalha na operação! Valor inválido")
            sleep(2)
            return False
        

class AccountIterator:
    def __init__(self, accounts: Account) -> None:
        self.accounts = accounts
        self.index = 0


    def __iter__(self):
        return self


    def __next__(self):
        try:
            account = self.accounts[self.index]
            return f"""
            Agência:\t{account.agency}
            Número:\t\t{account.account_id}
            Titular:\t{account.customer.name}
            Saldo:\t\tR$ {account.balance:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self.index += 1
