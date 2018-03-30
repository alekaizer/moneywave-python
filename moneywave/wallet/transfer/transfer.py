class Transfer:
    def __init__(self, util):
        self.util = util

    def to_wallet(self, source_wallet, recipient_wallet, amount, currency,
                  lock):
        data = {"sourceWallet": source_wallet,
                "recipientWallet": recipient_wallet,
                "amount": amount, "currency": currency, "lock": lock}
        return self.util.send_request(self.util.settings.transfer_wallet, data)

    def to_account(self, sender_name, ref, account_number,
                   bank_code, amount, currency, lock, narration=None):
        """
        :param sender_name: the name of the sender
        :param ref: unique transaction reference
        :param account_number: the account number of the recipient
        :param bank_code: the bankcode of the bank to send money to
        :param amount: the amount to send to the beneficiary
        :param currency: the currency to send money in
        :param lock: the password of your wallet
        :param narration: Narration is a key for disbursements as it gives more
         details to your transactions
        :return:
        """
        data = {"senderName": sender_name, "accountNumber": account_number,
                "bankcode": bank_code, "amount": amount, "currency": currency,
                "ref": ref, "lock": lock}
        if narration:
            data['narration'] = narration
        return self.util.send_request(self.util.settings.transfer_account, data)

    def to_account_bulk(self, sender_name, ref, name, recipients, lock,
                        currency=None):
        if not isinstance(recipients):
            raise TypeError('recipients should be a list')
        else:
            valid = [True for x in recipients if (
            'amount' in x and 'bankcode' in x and 'accountNumber' in x)]
            if len(valid) != len(recipients):
                raise ValueError(
                    'recipents objects should be {"amount": amount, '
                    '"bankcode": bankcode, "accountNumber": account_number}')

        data = {'senderName': sender_name, 'name': name, 'lock': lock,
                'ref': ref,
                'recipients': recipients, 'instantQueue': True}
        if currency:
            data['currency'] = currency

        return self.util.send_request(self.util.settings.transfer_account_bulk,
                                      data)
