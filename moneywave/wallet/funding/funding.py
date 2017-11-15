class Funding:
    def __init__(self, util):
        self.util = util

    def pay_with_internet_bank(self, first_name, last_name, phone_number, email,
                               recipient_id, sender_bank, amount,
                               medium, redirect_url):

        data = {"firstname": first_name, "lastname": last_name, "email": email,
                "phonenumber": phone_number, "recipient": "wallet",
                "recipient_id": recipient_id, "amount": amount,
                "sender_bank": sender_bank,
                "medium": medium, "redirecturl": redirect_url,
                "charge_auth": "INTERNETBANKING",
                "charge_with": "ext_account",
                "apiKey": self.util.settings.api_key}
        return self.util.send_request(self.util.settings.funding_pay, data)

    def account_to_wallet(self, first_name, last_name, phone_number, email,
                          sender_account_number, sender_bank, amount,
                          redirect_url):

        data = {"firstname": first_name, "lastname": last_name, "email": email,
                "phonenumber": phone_number, "recipient": "wallet",
                "sender_account_number": sender_account_number,
                "amount": amount, "sender_bank": sender_bank,
                "redirecturl": redirect_url, "charge_auth": "INTERNETBANKING",
                "charge_with": "account", "apiKey": self.util.settings.api_key}

        return self.util.send_request(self.util.settings.account_transfer, data)

    def account_to_wallet_validation(self, transaction_ref, otp=None,
                                     account_credit=None):
        if not (otp or account_credit):
            raise Exception('OTP or ACCOUNT_CREDIT value is required')
        else:
            auth_type = "OTP" if otp else "ACCOUNT_CREDIT"
            auth_value = otp or account_credit
        data = {"transactionRef": transaction_ref, "authType": auth_type,
                "authValue": auth_value}

        return self.util.send_request(self.util.settings.funding_charge_account,
                                      data)

    def card_to_wallet(self, first_name, last_name, phone_number, email,
                       recipient,
                       recipient_id, card_no, expiry_year, expiry_month, cvv,
                       amount, fee, redirect_url, medium="mobile",
                       narration=None, is_mastercard=False):
        charge_with = "card"
        charge_auth = "PIN" if is_mastercard else None
