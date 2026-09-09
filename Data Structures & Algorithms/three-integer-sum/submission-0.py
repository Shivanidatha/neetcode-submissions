class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                cursum=nums[i]+nums[l]+nums[r]
                if cursum>0:
                    r-=1
                elif cursum<0:
                    l+=1
                else:
                    ans.append([nums[l],nums[r],nums[i]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return ans