class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        maxL, maxR = 0, 0 
        l = 0
        for r in range(len(nums)):
            if currSum < 0:
                currSum = 0
                l = r
            currSum += nums[r]
            maxSum = max(currSum,maxSum)
            maxL = l
            maxR = r
        return maxSum