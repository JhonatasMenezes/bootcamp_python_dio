from .transaction import Transaction
from .account_interface import AccountInterface

class GetMoney(Transaction):
    def __init__(self, value: float) -> None:
        self.__value = value


    @property
    def value(self):
        return self.__value


    def record_transaction(self, account: AccountInterface) -> None:
        transaction_success = account.cash_out(self.value)

        if transaction_success:
            account.records.add_transaction(self)
