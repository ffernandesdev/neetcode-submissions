class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        mp = 0

        for r in range(1, len(prices)):
            p = prices[r] - prices[l]
            if p > mp:
                mp = p
            if prices[r] < prices[l]:
                l = r
        
        return mp

        

