class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProf = max(maxProf,profit)
        return maxProf

            
