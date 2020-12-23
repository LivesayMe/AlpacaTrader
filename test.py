import alpaca_trade_api as tradeapi
import datetime


apiKey = "AK0NH0Q7BUUANZ2E2GKL"
secretKey = "v1pokxWFX12BRujjOomxmownZnWE0e6eIcxtndfR"
realEndpoint = "https://api.alpaca.markets"

paperEndpoint = "https://paper-api.alpaca.markets"
paperKey = "PKW2JHY75SLSKA1VUX74"
paperSecret = "mS59yaHEGv5CyBFmaGqrmziRRkF14ioEWS8ENmGG"


class Trader:
    def __init__(self):
        self.alpaca = tradeapi.REST(paperKey, paperSecret, paperEndpoint, 'v2')

        stockUniverse = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA', 'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW', 'OKTA', 'TWTR', 'TM', 'RTN', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM', ]
        # Format the allStocks variable for use in the class.
        self.allStocks = []
        for stock in stockUniverse:
            self.allStocks.append([stock, 0])

    def run(self):
        self.submitOrder(5,self.allStocks[0][0], "buy", [])

    # Submit an order if quantity is above 0.
    def submitOrder(self, qty, stock, side, resp):
        if(qty > 0):
            try:
                self.alpaca.submit_order(stock, qty, side, "market", "day")
                print("Market order of | " + str(qty) + " " + stock + " " + side + " | completed.")
                resp.append(True)
            except:
                print("Order of | " + str(qty) + " " + stock + " " + side + " | did not go through.")
                resp.append(False)
        else:
            print("Quantity is 0, order of | " + str(qty) + " " + stock + " " + side + " | not completed.")
            resp.append(True)

# Run the LongShort class
ls = Trader()
ls.run()
