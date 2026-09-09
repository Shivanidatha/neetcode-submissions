class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        ans=0
        while l<r and r<len(prices):
            if prices[l]>prices[r]:
                l=r
            else:
                profit=prices[r]-prices[l]
                ans=max(ans,profit)
            r+=1
        return ans