class Account:
    def __init__(self, util):
        self.util = util

    def card_to_account(self, first_name, last_name, phone_number, email,
                        recipient_bank_account, recipient_bank_code,
                        card_no, exp_year, exp_month, cvv,
                        amount, fee, redirect_url, medium="mobile",
                        narration=None, pin=None):
        is_verve, is_local_mastercard = self.check_card_type(card_no)

        data = {
            "firstname": first_name, "lastname": last_name,
            "phonenumber": phone_number, "recipient": "account",
            "email": email, "card_no": card_no, "cvv": cvv,
            "expiry_month": exp_month, "expiry_year": exp_year,
            "recipient_bank": recipient_bank_code,
            "recipient_account_number": recipient_bank_account,
            "amount": amount, "fee": fee, "medium": medium,
            "redirecturl": redirect_url
        }
        if is_verve:
            if pin:
                data["pin"] = pin
            else:
                raise Exception('VERVE Cards required pin')
        elif is_local_mastercard:
            data["charge_with"] = "card"
            data["charge_auth"] = "PIN"
        if narration:
            data["narration"] = narration
        response = self.util.send_request(self.util.settings.account_transfer,
                                          data)
        return response

    def card_to_account_validation(self, transaction_ref, otp):
        data = {'transactionRef': transaction_ref, 'otp': otp}
        response = self.util.send_request(
            self.util.settings.account_verification, data)
        return response

    def check_card_type(self, card_no):
        response = self.util.send_request(self.util.settings.card_enquiry,
                                          {"cardNumber": card_no})
        is_verve, is_local_mastercard = False, False
        if 'data' in response:
            if response.get('data').get('cardType') == "VERVE":
                is_verve = True
            elif response.get('data').get(
                    'cardType') == "LOCAL" and response.get('data').get(
                    'cardBrand') == "MASTERCARD":
                is_local_mastercard = True

        return is_verve, is_local_mastercard
