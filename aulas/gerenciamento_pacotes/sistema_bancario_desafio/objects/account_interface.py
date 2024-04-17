from abc import ABC, abstractmethod


class AccountInterface(ABC):

    @abstractmethod
    def new_account(self):
        pass

    @abstractmethod
    def cash_out(self, value: float) -> bool:
        pass

    @abstractmethod
    def deposit(self, value: float) -> bool:
        pass
