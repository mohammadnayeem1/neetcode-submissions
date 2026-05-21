class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counterS = Counter(s)
        counterT = Counter(t)
        return counterS == counterT
        

        