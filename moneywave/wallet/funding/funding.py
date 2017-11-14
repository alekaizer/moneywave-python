class Funding:
    def __init__(self, util):
        self.util = util

    def pay_with_internet_bank(self, first_name, last_name, phone_number, email,
                               recipient, recipient_id, sender_bank, amount, redirect_url):
        charge_auth = "INTERNETBANKING"
        charge_with = "ext_account"
        medium = "mobile"
        pass

    def account_to_wallet(self, first_name, last_name, phone_number, email,
                               recipient, recipient_id, sender_bank, amount, redirect_url):
        charge_with = "ext_account"
        medium = "mobile"
        pass

    def account_to_wallet_validation(self, transaction_ref, otp=None, account_credit=None):
        if not (otp or account_credit):
            raise Exception('OTP or ACCOUNT_CREDIT value is required')
        else:
            auth_type = "OTP" if otp else "ACCOUNT_CREDIT"
            auth_value = otp or account_credit
        pass

    def card_to_wallet(self, first_name, last_name, phone_number, email, recipient,
                       recipient_id, card_no, expiry_year, expiry_month, cvv,
                       amount, fee, redirect_url, medium="mobile",
                       narration=None, is_mastercard=False):
        charge_with = "card"
        charge_auth = "PIN" if is_mastercard else None