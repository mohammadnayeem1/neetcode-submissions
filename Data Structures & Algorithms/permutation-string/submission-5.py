from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        goal = Counter(s1)
        window = Counter()

        for r in range(len(s2)):
            window[s2[r]] += 1
            if goal == window:
                return True
            if r-l+1 >= len(s1):
                if window[s2[l]] == 0:
                    del window[s2[l]]
                else:
                    window[s2[l]] -= 1
                l += 1
        return False