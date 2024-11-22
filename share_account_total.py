
class PriceOfShare:
    def __init__(self):
        self.price_of_share = []

    
    def add_share_data(self, ticker, share_price):
        self.price_of_share.append((ticker, share_price))
        return 

    def get_share_data(self):
        return self.price_of_share


class ShareAccount:
    def __init__(self):
        self.share_account = []


    def add_account_data(self, account_number, ticker, number_of_shares):
        self.share_account.append((account_number, ticker, number_of_shares))
        return     


    def get_account_data(self):
        return self.share_account
    

if __name__ == "__main__":

    price_of_share = PriceOfShare()
    account = ShareAccount()

    ticker_sum_dict =  {}
    account_sum_dict = {}

    price_of_share.add_share_data("WALM", 4)
    price_of_share.add_share_data("AAPL", 1)
    price_of_share.add_share_data("GOOL", 2)
    price_of_share.add_share_data("NVID", 5)
    price_of_share.add_share_data("AMZ", 3)

    account.add_account_data("2abc03", "NVID", 10)
    account.add_account_data("54ac7c", "WALM", 10)
    account.add_account_data("2abc03", "AAPL", 15)
    account.add_account_data("4cd6f0", "GOOL", 20)
    account.add_account_data("54ac7c", "NVID", 30)
    account.add_account_data("2abc03", "AMZ", 35)
    account.add_account_data("54ac7c", "AAPL", 13)
    account.add_account_data("54ac7c", "AMZ", 16)
    account.add_account_data("4cd6f0", "NVID", 50)

    for ticker, price in price_of_share.get_share_data():
        ticker_sum_dict[ticker] = price
    
    for acc, ticker, price in account.get_account_data():
        if ticker in ticker_sum_dict:
            ticker_total = ticker_sum_dict[ticker] * price
        
        account_sum_dict[acc] = ticker_total + account_sum_dict.get(acc,0)
    
    print(account_sum_dict)