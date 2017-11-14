class Account:
    def __init__(self, util):
        self.util = util

    def card_to_account(self, first_name, last_name, phone_number, email,
                       recipient_bank_account, recipient_bank_code,
                        card_no, expiry_year, expiry_month, cvv,
                       amount, fee, redirect_url, medium="mobile",
                       narration=None, is_mastercard=False):
        charge_with = "card"
        charge_auth = "PIN" if is_mastercard else None
        recipient = "account"
        pass

    def card_to_account_validation(self, transaction_ref, otp):
        pass