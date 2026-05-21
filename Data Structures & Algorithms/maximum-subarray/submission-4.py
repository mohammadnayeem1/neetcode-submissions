class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        res = nums[0]
        for num in nums:
            currSum = max(currSum,0)
            currSum += num
            res = max(currSum,res)
        return res
        