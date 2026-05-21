class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Set = Counter(s1)
        s2Set = Counter()
        l = 0
        for r in range(len(s2)):
            s2Set[s2[r]] += 1
            if r >= len(s1)-1:
                if s1Set == s2Set:
                    return True
                s2Set[s2[l]] -= 1
                l += 1
        return False