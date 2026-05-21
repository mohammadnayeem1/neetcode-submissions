class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = float("inf"),None,None
        formed = 0
        tCounter = Counter(t)
        sCounter = Counter()
        for r in range(len(s)):
            sCounter[s[r]] += 1
            if s[r] in tCounter and sCounter[s[r]] == tCounter[s[r]]:
                formed +=1
            while l<=r and formed == len(tCounter):
                if res[0] > r-l+1:
                    res = (r-l+1,l,r)
                sCounter[s[l]] -= 1
                if s[l] in tCounter and sCounter[s[l]] < tCounter[s[l]]:
                    formed -=1
                l += 1
        return "" if res[0] ==  float("inf") else s[res[1]:res[2]+1]