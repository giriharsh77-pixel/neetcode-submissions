class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns=len(s)
        nt=len(t)

        if ns!=nt:
            return False
        else:
            countS,countT = {},{}
            for i in range(ns):
                countS[s[i]]=1+ countS.get(s[i],0)
                countT[t[i]]=1+ countT.get(t[i],0)

            for c in countS:
                if countS[c]!= countT.get(c,0):
                    return False

            return True






        