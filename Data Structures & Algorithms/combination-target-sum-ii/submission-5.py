class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr=[]
        def dfs(i,curr,target):
            if target == 0:
                res.append(curr.copy())
                return
            if i >= len(candidates) or target < 0:
                return
            curr.append(candidates[i])
            target -= candidates[i]
            dfs(i+1,curr,target)
            target += candidates[i]
            while i < len(candidates)- 1 and candidates[i] == candidates[i+1]:
                i += 1
            curr.pop()
            dfs(i+1,curr,target)
        dfs(0,curr,target)
        return res