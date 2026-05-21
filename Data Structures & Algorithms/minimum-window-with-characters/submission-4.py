class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = len(s)+1,None,None
        tCount = Counter(t)
        sCount = Counter()
        l = 0
        formed = 0
        for r in range(len(s)):
            sCount[s[r]] += 1
            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                formed += 1
            while l<=r and formed == len(tCount):
                if r-l+1 < res[0]:
                    res = (r-l+1,l,r)
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    formed -=1
                l += 1
        return "" if res[0] == len(s)+1 else s[res[1]:res[2]+1]

