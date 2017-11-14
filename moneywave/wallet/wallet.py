from moneywave.wallet.funding import Funding
from moneywave.wallet.transfer import Transfer


class Wallet:
    def __init__(self, util):
        self.util = util
        self.funding = Funding(util)
        self.transfer = Transfer(util)

    def get_balance(self):
        pass

    def create_sub_wallet(self):
        pass