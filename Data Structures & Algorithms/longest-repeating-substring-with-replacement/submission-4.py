class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        l = 0
        res = 1
        for r in range(len(s)):
            hm[s[r]] += 1
            while (r-l+1) - max(hm.values()) > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res