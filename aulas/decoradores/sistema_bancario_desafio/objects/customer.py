from typing import Dict
from .account_interface import AccountInterface
from .transaction import Transaction

class Customer:
    def __init__(self, adress: Dict) -> None:
        self.__adress = adress
        self.__accounts = []
    
    
    @property
    def accounts(self):
        return self.__accounts


    @classmethod
    def execute_transaction(cls, account: AccountInterface, transaction: Transaction):
        if len(account.records.day_transactions()) >= 10:
            print("\n Você excedeu o número de transações permitidas para hoje!")
            return
        transaction.record_transaction(account)


    def add_account(self, account):
        self.__accounts.append(account)

