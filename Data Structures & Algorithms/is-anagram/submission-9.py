class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = Counter(s)
        tMap = Counter(t)
        if sMap == tMap:
            return True
        for letter in s:
            if letter in tMap:
                tMap[letter] -= 1
                if tMap[letter] == 0:
                    del tMap[letter]
            else:
                return False
        return len(tMap) == 0