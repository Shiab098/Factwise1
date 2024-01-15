class Answer:
    def maxProfit(self,price):
        profit  = 0 
        buy = price[0]
        for sell in price[1:]:
            if sell > buy :
                profit = max(profit,sell-buy)
            else:
                buy = sell
        return profit
        