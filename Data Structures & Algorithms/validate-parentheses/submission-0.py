class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for c in s:
            if c in pMap:
                stack.append(pMap[c])
            else:
                if not stack or stack.pop() != c:
                    return False
        return not stack
            