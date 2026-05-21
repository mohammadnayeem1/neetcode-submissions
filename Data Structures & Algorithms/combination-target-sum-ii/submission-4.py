class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr = [] , []
        def dfs(i):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or sum(curr) > target:
                return
            curr.append(candidates[i])
            dfs(i+1)
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            curr.pop()
            dfs(i +1)
        dfs(0)
        return res