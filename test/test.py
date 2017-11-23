from moneywave import MoneyWave
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=3)

ACCESS_BANK = "0690000004"
PROVIDUS_BANK = 5900102340
UNITY_BANK = "0025756133"
OTP_BANK = 12345

API_KEY = "YOUR_API_KEY"
SECRET = "YOUR_SECRET_KEY"
CARDS = {
    "verve": {'no': "5061020000000000094", 'cvv': 347, 'exp_m': "07",
              'exp_y': 20, 'pin': 111, 'otp': 123456},
    "visa": {'no': "4242424242424242", 'cvv': 812, 'exp_m': "01", 'exp_y': 19,
             'pin': 3310, 'otp': 12345},
    "mastercard": {'no': '5438898014560229', 'cvv': 789, 'exp_m': "09",
                   'exp_y': 19, 'pin': 3310, 'otp': 12345},
    "visa_local": {'no': '4187427415564246', 'cvv': 828, 'exp_m': '09',
                   'exp_y': 19, 'pin': 3310, 'otp': 12345},
    "visa_international": {'no': '4556052704172643', 'cvv': 899, 'exp_m': '01',
                           'exp_y': 19}
}
TEST_CARD_VERVE = "5061020000000000094"
TEST_CARD_VISA = "4242424242424242"

EXP_M = "07"
EXP_Y = "20"
CVV = 347
PIN = 111
OTP = 123456

API = MoneyWave(API_KEY, SECRET)
"""
print("======== GET BALANCE ========")
r = API.Wallet.get_balance()
pp.pprint(r)

print("======= CREATE SUB WALLET =======")
# r = API.Wallet.create_sub_wallet("Johnny", "sayWHAAATT!",
# "cus_0399292", "NGN")
# pp.pprint(r)


print("======= CREATE CARD ========")
r = API.Resource.create_card(TEST_CARD_VERVE, EXP_M, EXP_Y, CVV)
pp.pprint(r)

print("======= CARD INFOS ========")
r = API.Resource.card_details(TEST_CARD_VERVE)
pp.pprint(r)


print("======== CREDIT WALLET =======")
rr = API.Wallet.funding.card_to_wallet("John", "Doe", "+2348122681468",
                                       "johnny.deezy@gmail.com", "c_0093934nk",
                                       CARDS.get('visa').get('no'),
                                       CARDS.get('visa').get('exp_m'),
                                       CARDS.get('visa').get('exp_y'),
                                       CARDS.get('visa').get('cvv'), 300, 35,
                                       "https://google.fr", "mobile")
pp.pprint(rr)
"""