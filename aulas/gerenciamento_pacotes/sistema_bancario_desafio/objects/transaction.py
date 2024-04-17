from abc import ABC, abstractmethod

from .account_interface import AccountInterface


class Transaction(ABC):

    @abstractmethod
    def record_transaction(self, account: AccountInterface):
        pass
