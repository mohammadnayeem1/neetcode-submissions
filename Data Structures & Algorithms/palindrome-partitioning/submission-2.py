class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def dfs(i,curr):
            if i == len(s):
                res.append(curr.copy())
                return
            for j in range(i,len(s)):
                if self.isPali(i,j,s):
                    curr.append(s[i:j+1])
                    dfs(j+1,curr)
                    curr.pop()
        dfs(0,curr)
        return res


    def isPali(self,left,right,s):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
        return True