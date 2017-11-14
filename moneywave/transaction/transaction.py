class Transaction:
    def __init__(self, util):
        self.util = util

    def get_total_amount(self, amount, merchant_fee=0):
        pass

    def retry_disburse(self, charge_id, recipient_account_number, recipient_bank):
        pass

    def get_transaction(self, transaction_id=None, ref=None, source="card"):
        if source == "card":
            if not transaction_id:
                raise Exception('Missing transaction_id')
            else:
                pass
            pass
        elif source == "wallet":
            if not ref:
                raise Exception('Missing ref')
            else:
                pass
        else:
            raise Exception('Unknown source. '
                            'Source can be either "card" or "wallet"')

    def transaction_status(self, ref):
        pass