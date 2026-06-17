class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        
        for i in range(len(prices)):
            for c in range(len(prices)):
                if c <= i:
                    continue
                if i < c:
                    if prices[c] - prices[i] >= profit:
                        profit = prices[c] - prices[i]
            
        if profit < 0:
            profit = 0

        return profit


        
    


   
        


            