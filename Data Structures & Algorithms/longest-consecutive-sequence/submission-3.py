class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen=set(nums)
        res=0
        for i in nums:
            if i-1 not in seen:
                ans=1
                while i+1 in seen:
                    ans+=1
                    i+=1
                res=max(ans,res)
        return res

        