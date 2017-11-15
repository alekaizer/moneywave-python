charge_response_codes = {
    "0": "Successful",
    "00": "Successful",
    "0-M": "Verification attempted",
    "0-Y": "Verification Successful",
    "RR-V": "Transaction already validated.",
    "02": "Needs card Validation",
    "RR": "Transaction Failed. Detailed Message is included in response message",
    "2": "Declined",
    "7": "Card Declined due to invalid card data",
    "RR-T2": "Card not enrolled for safe token, user should contact their bank",
    "XS0": "Authorization Failed due to connectivity issues with the bank",
    "B01": "Invalid BVN",
    "RR-51": "Insufficient Funds",
    "RR-R3": "CardToken is mandatory!",
    "RR-14": "Invalid Card Number",
    "RR-55": "Incorrect PIN",
    "R0": "Transaction Failed due to connectivity issues with the bank",
    "RR-E42": "Card Declined due to invalid card expiry",
    "RR-56": "No Card Record",
    "RR-2": "Card Declined",
    "RR-X04": "Transaction Amount too low",
    "RR-15": "Transaction error",
    "RR-7": "Card Declined due to invalid card security code",
    "RR-57": "Transaction not Permitted to Cardholder",
    "RR-04": "Pick-up card",
    "RR-Z8": "Payment Gateway currently does not accept your card type",
    "RR-91": "Bank or switch network error",
    "EEE": "An unexpected error occurred!",
    "RR-E18": "The service provider is unreachable at the moment, please try "
              "again later.",
    "RR-E19": "An invalid response was received from remote host, see provider "
              "response code/message for details.",
    "RR-E32": "JSON is badly formatted or it contains invalid character.",
    "RR-E57": "The PIN contains an invalid character",
    "RR-EE4": "Card Details could not be Retrieved!",
    "RR-R401": "Card has been blocked due to too many failed retries.",
    "N-E": "Card not enrolled for 3DSecure",
    "BR0": "Timeout on BVN check",
    "RN0": "Invalid Account"
}

disburse_response_codes = {
    "400": "Bad Request – Your request sucks",
    "401": "Unauthorized – Your API key is wrong",
    "403": "Forbidden – The endpoint requested is hidden for administrators"
           " only",
    "404": "Not Found – The specified endpoint could not be found",
    "405": "Method Not Allowed – You tried to access an endpoint with an "
           "invalid method",
    "406": "Not Acceptable – You requested a format that isn’t json",
    "410": "Gone – The endpoint requested has been removed from our servers",
    "429": "Too Many Requests!",
    "500": "Internal Server Error – We had a problem with our server. Try again"
           " later.",
    "503": "Service Unavailable – We’re temporarily offline for maintenance."
           " Please try again later."
}


class Settings:
    def __init__(self, api_key, secret_key, mode="live"):
        self.api_key = api_key
        self.secret_key = secret_key

        if mode == "test":
            self.url = "https://moneywave.herokuapp.com"
        else:
            self.url = "https://live.moneywaveapi.co/"
        self.access_token = "/v1/merchant/verify"
        self.account_transfer = "/v1/transfer"
        self.account_charge_card = "/v1/transfer/charge/auth/card"
        self.funding_pay = "/v1/transfer"
        self.funding_charge_account = "/v1/transfer/charge/auth/account"
        self.funding_charge_card = self.funding_pay
        self.transfer_wallet = "/v1/wallet/transfer"
        self.transfer_account = "/v1/disburse"
        self.transfer_account_bulk = "/v1/disburse/queue"
        self.resource_banks = "/v1/banks"
        self.account_verification = "/v1/resolve/account"
        self.card_tokenization = "/v1/transfer/charge/tokenize/card"
        self.card_enquiry = "/v1/user/card/check"
        self.reporting = "/v1/report/transactions"
        self.transaction_get_total = "/v1/get-charge"
        self.transaction_retrial = "/v1/transfer/disburse/retry"
        self.transaction_previous_card = "/v1/transfer/{0}"
        self.transaction_status = "/v1/transfer/charge/status"
        self.transaction_wallet = "/v1/disburse/status"
        self.get_balance = "/v1/wallet"
        self.create_wallet = self.get_balance

    # noinspection PyMethodMayBeStatic
    def get_error_msg(self, code):
        return charge_response_codes.get(code) or disburse_response_codes.get(
            code) or 'Unknown Error'
