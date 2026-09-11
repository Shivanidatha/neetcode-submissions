class Solution:
    def isValid(self, s: str) -> bool:
        hm= { ')': '(', '}': '{', ']':'['}

        st=[]
        for i in range(len(s)):
            if s[i] not in hm:
                st.append(s[i])
            else:
                if not st or st.pop()!= hm[s[i]]:
                    return False
        return not st