class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr = [] , []
        self.backTrack(0,res,curr,candidates,target)
        return res

    def backTrack(self,i,res,curr,candidates,target):
        if target == sum(curr) and curr not in res:
            res.append(curr.copy())
            return
        if i>len(candidates)-1 or sum(curr) > target:
            return
        curr.append(candidates[i])
        self.backTrack(i+1,res,curr,candidates,target)
        curr.pop()
        self.backTrack(i+1,res,curr,candidates,target)
