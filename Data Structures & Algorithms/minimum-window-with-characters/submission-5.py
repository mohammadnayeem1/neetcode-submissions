class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = (len(s) + 1, None, None)
        tCounter = Counter(t)
        sCounter = Counter()
        l = 0
        formed = 0
        for r in range(len(s)):
            sCounter[s[r]] += 1
            if s[r] in t and sCounter[s[r]] == tCounter[s[r]]:
                formed += 1
            while l<=r and formed == len(tCounter):
                if (r-l+1) < res[0]:
                    res = (r-l+1,l,r)
                sCounter[s[l]] -= 1
                if s[l] in t and sCounter[s[l]] < tCounter[s[l]]:
                    formed -= 1 
                l += 1
        return "" if res[0] == len(s) + 1 else s[res[1]:res[2]+1]
