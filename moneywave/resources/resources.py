class Resource():
    def __init__(self, util):
        self.util = util

    def get_banks(self):
        pass

    def validate_account(self, account_number, bank_code):
        pass

    def create_card(self,card_number, expiry_year, expiry_month, cvv):
        pass

    def card_details(self, card_number):
        pass

    def get_reports(self, status="completed", amount=0, flwref="", ref="",
                    date="", currency="NGN", type="credit", limit=None,
                    page=None):
        pass

