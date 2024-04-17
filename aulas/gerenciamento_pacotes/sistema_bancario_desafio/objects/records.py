from datetime import datetime

from .transaction import Transaction


class Records:
    def __init__(self) -> None:
        self.__transactions = []

    @property
    def transactions(self):
        return self.__transactions

    def add_transaction(self, transaction: Transaction):
        date_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.__transactions.append(
            {
                "date_time": date_now,
                "transaction_type": transaction.__class__.__name__,
                "value": transaction.value,
            }
        )

    def generate_report(self, transaction_type=None):
        for transaction in self.transactions:
            if (
                transaction_type is None
                or transaction[transaction_type] == transaction_type
            ):
                yield transaction

    def day_transactions(self):
        date_now = datetime.now().date()
        transactions = []
        for transaction in self.transactions:
            transaction_date = datetime.strptime(
                transaction["date_time"], "%d-%m-%Y %H:%M:%S"
            ).date()
            if date_now == transaction_date:
                transactions.append(transaction)

        return transactions
