class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0 
        minp=float('inf')
        for p in prices:
            minp=min(minp, p)
            maxprofit=max(maxprofit, p-minp)

        return maxprofit
            
