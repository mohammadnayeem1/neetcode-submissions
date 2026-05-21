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
                if not stack:
                    return False
                if stack.pop() != c:
                    return False
        return len(stack) == 0