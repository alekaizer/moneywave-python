from datetime import datetime


class Resource:
    def __init__(self, util):
        self.util = util

    def get_banks(self):
        return self.util.send_request(self.util.settings.resource_banks, {})

    def validate_account(self, account_number, bank_code):
        data = {"account_number": account_number, "bank_code": bank_code}
        return self.util.send_request(self.util.settings.account_verification,
                                      data)

    def create_card(self, card_number, expiry_year, expiry_month, cvv):
        data = {"card_no": card_number, "expiry_year": expiry_year,
                "expiry_month": expiry_month, "cvv": cvv}
        return self.util.send_request(self.util.settings.card_tokenization,
                                      data)

    def card_details(self, card_number):
        data = {"card_no": card_number}
        return self.util.send_request(self.util.settings.card_enquiry, data)

    def get_reports(self, status, amount, flutterwave_ref, ref, currency="NGN",
                    date=datetime.today(), limit=None, page=None,
                    type="credit"):
        data = {"status": status, "amount": amount, "flwref": flutterwave_ref,
                "ref": ref, "currency": currency, "date": date, "type": type}
        if limit:
            data['limit'] = limit
        if page:
            data['page'] = page

        return self.util.send_request(self.util.settings.reporting, data)
