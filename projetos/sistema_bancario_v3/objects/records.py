from datetime import datetime
from .transaction import Transaction

class Records:
    def __init__(self) -> None:
        self.__transactions = []

    
    @property
    def transactions(self):
        return self.__transactions

    
    def add_transaction(self, transaction: Transaction):
        date_now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        self.__transactions.append(
            {
                "date_time": date_now,
                "transaction_type": transaction.__class__.__name__,
                "value": transaction.value
            }
        )