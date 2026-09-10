class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hm1=Counter(s1)
        hm2=Counter(s2[:len(s1)])
        l=0
        r=len(s1)
        while r<len(s2):
            if hm1==hm2:
                return True
            hm2[s2[l]]-=1
            l+=1
            hm2[s2[r]]=1+hm2.get(s2[r],0)
            r+=1
        return hm1==hm2



