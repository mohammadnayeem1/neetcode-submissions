class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        self.helper(0,nums,res,curr,target)
        return res
        
    def helper(self,i, nums,res,curr,target):
        if sum(curr) == target and curr not in res:
            res.append(curr.copy())
            return
        if i == len(nums) or sum(curr) > target:
            return
        curr.append(nums[i])
        self.helper(i,nums,res,curr,target)
        self.helper(i+1,nums,res,curr,target)
        curr.pop()
        self.helper(i+1,nums,res,curr,target)
