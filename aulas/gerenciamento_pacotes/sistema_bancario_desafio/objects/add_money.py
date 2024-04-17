from .account import AccountInterface
from .transaction import Transaction


class AddMoney(Transaction):
    def __init__(self, value: float) -> None:
        self.__value = value

    @property
    def value(self):
        return self.__value

    def record_transaction(self, account: AccountInterface) -> None:
        transaction_success = account.deposit(self.value)

        if transaction_success:
            account.records.add_transaction(self)
