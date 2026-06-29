class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS={}
        freqT={}

        for ch in s:
            freqS[ch]=freqS.get(ch,0)+1
        for ch in t:
            freqT[ch]=freqT.get(ch,0)+1

        return (freqS==freqT)
        






        