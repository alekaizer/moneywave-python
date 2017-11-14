from moneywave.account import Account
from moneywave.resources import Resource
from moneywave.transaction import Transaction
from moneywave.utils import Util, Settings
from moneywave.wallet import Wallet


class MoneyWave:
    def __init__(self, api_key, secret_key):
        self.settings = Settings(api_key, secret_key)
        self.util = Util(self.settings)
        self.accounts = Account(self.util)
        self.resources = Resource(self.util)
        self.wallets = Wallet(self.util)
        self.transactions = Transaction(self.util)

    def __get_auth_key(self):
        pass

    @property
    def token(self):
        return self.util.token
