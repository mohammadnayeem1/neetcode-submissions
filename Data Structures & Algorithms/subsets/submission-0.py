class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [],[]
        self.helper(0,nums,res,curr)
        return res


    def helper(self,i,nums,res,curr):
        if i == len(nums):
            res.append(curr.copy())
            return
        curr.append(nums[i])
        self.helper(i+1,nums,res,curr)
        curr.pop()
        self.helper(i+1,nums,res,curr)
