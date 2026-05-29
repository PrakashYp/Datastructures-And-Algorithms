

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    best_day = prices[0]
    max_profit = 0


    for i in range(len(prices)):
        best_day = min(best_day,prices[i]) 
        max_profit = max(max_profit,prices[i] - best_day)
        print(best_day    , max_profit)



    return max_profit




prices = [7,1,5,3,6,4]

print(maxProfit(prices))
