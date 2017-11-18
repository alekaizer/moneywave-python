from moneywave import MoneyWave
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=3)

API_KEY = "ts_WO5XX2RL5ZXIRYVV0PGH"
SECRET = "ts_6BGMZA72EI00WUQEN8EH3Y74H3HK3N"

API = MoneyWave(API_KEY, SECRET)

print("======== GET BALANCE ========")
r = API.Wallet.get_balance()
pp.pprint(r)

print("======= CREATE SUB WALLET =======")
#r = API.Wallet.create_sub_wallet("Achille", "cequejeveux", "cus_0399292", "NGN")
#pp.pprint(r)


print("======= CREATE CARD ========")
r = API.Resource.create_card("4242424242424242", 11, 21, 109)
pp.pprint(r)

print("======= CARD INFOS ========")
r = API.Resource.card_details("4242424242424242")
pp.pprint(r)
