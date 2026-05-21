class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #initiate max and curr counter and left pointer:
        maxSum = nums[0]
        currSum = 0
        #iterate through array index will be right pointer
        for r in range(len(nums)):
            #check if current sum greater than 0 if not reset sum and index
            currSum = max(currSum,0)
            #update curr sum
            currSum += nums[r]
            #find max between curr and max
            maxSum = max(currSum,maxSum)
        #return max
        return maxSum