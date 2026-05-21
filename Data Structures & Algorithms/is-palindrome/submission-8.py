class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
            lChar = s[l].lower()
            rChar = s[r].lower()
            if not lChar.isalnum():
                l += 1
                continue
            if not rChar.isalnum():
                r -=1
                continue
            if lChar != rChar:
                return False
            else:
                l += 1
                r -= 1
        return True