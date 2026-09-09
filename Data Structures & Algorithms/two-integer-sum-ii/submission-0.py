class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            cursum=numbers[l]+numbers[r]
            if target==cursum:
                return[l+1,r+1]
            elif target>cursum:
                l+=1
            else:
                r-=1
        return []