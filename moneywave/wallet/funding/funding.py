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
                       recipient_id, card_no, expiry_month,
                       expiry_year, cvv, amount, fee, redirect_url, medium,
                       narration=None, pin=None):
        is_verve, is_mastercard = self.check_card_type(card_no)
        if is_verve and not pin:
            raise Exception('Verve cards require PIN value, please set the '
                            'argument')
        data = {"firstname": first_name, "lastname": last_name, "email": email,
                "phonenumber": phone_number, "recipient": "wallet",
                "recipient_id": recipient_id, "card_no": card_no,
                "expiry_month": expiry_month, "expiry_year": expiry_year,
                "cvv": cvv, "apiKey": self.util.settings.api_key,
                "medium": medium, "charge_with": "card",
                "fee": fee, "amount": amount, "redirecturl": redirect_url}
        if narration:
            data['narration'] = narration
        if is_verve:
            data['pin'] = pin
        if is_mastercard:
            data['charge_with'] = "card"
            data['charge_auth'] = 'PIN'

        return self.util.send_request(self.util.settings.funding_pay, data)

    def card_to_wallet_with_token(self, first_name, last_name, phone_number, email,
                       recipient_id, card_token, amount, fee, redirect_url, medium):

        data = {"firstname": first_name, "lastname": last_name, "email": email,
                "phonenumber": phone_number, "recipient": "wallet",
                "recipient_id": recipient_id, "card_token": card_token,
                "apiKey": self.util.settings.api_key, "medium": medium,
                "charge_with": "tokenized_card", "fee": fee, "amount": amount,
                "redirecturl": redirect_url}
        print(data, "\n\n")
        # URL = "https://moneywave.herokuapp.com/v1/transfer"
        return self.util.send_request(self.util.settings.funding_pay, data)

    def card_details(self, card_number):
        data = {"cardNumber": card_number}
        return self.util.send_request(self.util.settings.card_enquiry, data)

    def check_card_type(self, card_no):
        response = self.util.send_request(self.util.settings.card_enquiry,
                                          {"cardNumber": card_no})
        is_verve, is_local_mastercard = False, False
        if 'data' in response:
            print("CARD INFOS", response.get('data'))
            if response.get('data').get('cardBrand') == "MAESTRO":
                is_verve = True
            elif response.get('data').get(
                    'countryOfIssueISO') == "NG" and response.get('data').get(
                    'cardBrand') == "MASTERCARD":
                is_local_mastercard = True

        return is_verve, is_local_mastercard
