from .customer import Customer
from .account import Account
from .get_money import GetMoney

class CurrentAccount(Account):
    def __init__(self, account_id: int, customer: Customer, limit=1000, cash_out_lmits=3) -> None:
        super().__init__(account_id, customer)
        self.__limit = limit
        self.__cash_out_lmits = cash_out_lmits
    
    def cash_out(self, value: float) -> bool:
        number_cash_outs = len(
            [transaction for transaction in self.records.transactions if transaction["transaction_type"] == GetMoney.__name__]
        )

        passed_limit = value > self.__limit
        passed_cash_outs = number_cash_outs >= self.__cash_out_lmits

        if passed_limit:
            print("Falha na operação! Valor maior que limite disponível.")
        
        elif passed_cash_outs:
            print("Falha na operação! Número máximo de saques excedido.")
        
        else:
            return super().cash_out(value)

        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agency}
            C/C:\t\t{self.account_id}
            Titular:\t{self.customer.name}
        """