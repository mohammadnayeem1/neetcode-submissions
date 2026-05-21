class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            lChar = s[l].lower()
            rChar = s[r].lower()
            if lChar.isalnum() == False:
                l += 1
                continue
            if rChar.isalnum() == False:
                r -=1
                continue
            if lChar != rChar:
                return False
            l += 1
            r -= 1
        return True


        