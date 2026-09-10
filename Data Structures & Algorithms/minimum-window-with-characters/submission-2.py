class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)< len(t):
            return ''
        hmt=Counter(t)
        hms={}
        l,r=0,0
        have=0
        required=len(hmt)
        ans=''
        minlen=float('inf')
        while r<len(s):
            hms[s[r]]=1+hms.get(s[r],0)
            if s[r] in hmt and hmt[s[r]]==hms[s[r]]:
                have+=1
            while have==required:
                if minlen>r-l+1:
                    minlen=r-l+1
                    ans=s[l:r+1]
                hms[s[l]]-=1
                if s[l] in hmt and hms[s[l]]<hmt[s[l]]:
                    have-=1
                l+=1
                
            r+=1
        return ans


