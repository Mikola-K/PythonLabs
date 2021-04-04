from modules.bank_service import BankService
from modules.deposit_type import DepositType
from modules.bank_type import BankType

class Deposit(BankService):
    def __init__(self, bank_name='', bank_type=BankType.COMERCIAL, is_available=False,
                 interest_rate=0.0, deposit_term=0.0, deposit_type=DepositType.ACCUMULATIVE):
        super().__init__(bank_name, bank_type, is_available, interest_rate)
        self.deposit_term = deposit_term
        self.deposit_type = deposit_type

    def __str__(self):
        return  f"{super().__str__()}\n"\
                f"Deposit term: {self.deposit_term}\n"\
                f"Deposit type: {self.deposit_type.name}\n"
