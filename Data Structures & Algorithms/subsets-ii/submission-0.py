class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        self.helper(0, nums, res, curr)
        return res

    def helper(self, i, nums, res, curr):
        if i == len(nums):
            res.append(curr.copy())
            return
        curr.append(nums[i])
        self.helper(i+1,nums,res,curr)
        curr.pop()
        while i < len(nums)-1 and nums[i] == nums[i+1]:
            i += 1
        self.helper(i+1,nums,res,curr)