class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r=0,0
        count=[0]*256
        ans=0
        while r<len(s):
            count[ord(s[r])]+=1
            while l<r and count[ord(s[r])]>1:
                count[ord(s[l])]-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans
