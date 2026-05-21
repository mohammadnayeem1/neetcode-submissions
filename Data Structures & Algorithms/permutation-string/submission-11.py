class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        goal = Counter(s1)
        window = Counter()
        winSize = len(s1)
        for r in range(len(s2)):
            window[s2[r]] += 1
            if r >= winSize:
                window[s2[r-winSize]] -=1
                if window[s2[r-winSize]] == 0:
                    del window[s2[r-winSize]]
            if goal == window:
                return True
        return False
