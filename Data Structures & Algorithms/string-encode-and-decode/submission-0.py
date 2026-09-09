class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for s in strs:
            ans+=str(len(s))+'#'+s
        return ans

    def decode(self, s: str) -> List[str]:
        i=0
        ans=[]
        while i<len(s):
            length=''
            curstr=''
            while s[i]!='#':
                length+=s[i]
                i+=1
            length=int(length)
            i+=1
            for _ in range(length):
                curstr+=s[i]
                i+=1
            ans.append(curstr)
        return ans

