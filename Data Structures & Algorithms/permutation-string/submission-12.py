class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = Counter()
        goal = Counter(s1)
        l = 0
        for r, c in enumerate(s2):
            seen[c] += 1
            if r >= len(s1)-1:
                if seen == goal:
                    return True
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1
        return False