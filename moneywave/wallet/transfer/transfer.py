class Transfer:
    def __init__(self, util):
        self.util = util

    def to_wallet(self, source_wallet, recipient_wallet, amount, currency, lock):
        pass

    def to_account(self, sender_name, ref, narration, account_number,
                   bank_code, amount, currency, lock):
        pass

    def to_account_bulk(self, sender_name, ref, name, recipients, currency, lock):
        instant_queue = True
        pass
