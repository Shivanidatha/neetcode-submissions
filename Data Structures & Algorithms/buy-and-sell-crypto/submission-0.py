class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowprice=float('inf')
        ans=0
        for i in range(len(prices)):
            if prices[i]<lowprice:
                lowprice=prices[i]
            profit=prices[i]-lowprice
            ans=max(ans,profit)
        return ans
