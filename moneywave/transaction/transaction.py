class Transaction:
    def __init__(self, util):
        self.util = util

    def get_total_amount(self, amount, merchant_fee=0):
        data = {"amount": amount, "fee": merchant_fee}
        return self.util.send_request(self.util.settings.transaction_get_total,
                                      data)

    def retry_disburse(self, charge_id, recipient_account_number,
                       recipient_bank):
        data = {"id": charge_id,
                "recipient_account_number": recipient_account_number,
                "recipient_bank": recipient_bank}
        return self.util.send_request(self.util.settings.transaction_retrial,
                                      data)

    def get_transaction(self, transaction_id=None, ref=None, source="card"):
        if source == "card":
            if not transaction_id:
                raise Exception('Missing transaction_id')
            else:
                response = self.util.send_request(
                    self.util.settings.transaction_previous_card.format(
                        transaction_id), {})
        elif source == "wallet":
            if not ref:
                raise Exception('Missing ref')
            else:
                data = {'ref': ref}
                response = self.util.send_request(
                    self.util.settings.transaction_wallet, data)
        else:
            raise Exception('Unknown source. '
                            'Source can be either "card" or "wallet"')
        return response

    def transaction_status(self, ref):
        return self.util.send_request(self.util.settings.transaction_status,
                                      {"ref": ref})
