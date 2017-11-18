from moneywave.account import Account
from moneywave.resources import Resource
from moneywave.transaction import Transaction
from moneywave.utils import Util, Settings
from moneywave.wallet import Wallet


class MoneyWave:
    def __init__(self, api_key, secret_key, mode="test"):
        self.settings = Settings(api_key, secret_key, mode)
        self.__util = Util(self.settings)
        self.Account = Account(self.__util)
        self.Resource = Resource(self.__util)
        self.Wallet = Wallet(self.__util)
        self.Transaction = Transaction(self.__util)

    def __get_auth_key(self):
        pass

    @property
    def token(self):
        return self.__util.token
