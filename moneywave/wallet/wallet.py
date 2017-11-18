from moneywave.wallet.funding import Funding
from moneywave.wallet.transfer import Transfer


class Wallet:
    def __init__(self, util):
        self.util = util
        self.funding = Funding(util)
        self.transfer = Transfer(util)

    def get_balance(self):
        return self.util.send_request(self.util.settings.get_balance, None, method="get")

    def create_sub_wallet(self, name, lock_code, user_ref, currency):
        data = {"name": name, "lock_code": lock_code, "user_ref": user_ref,
                'currency': currency}
        return self.util.send_request(self.util.settings.create_wallet, data)