class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k-1
        highest = max(nums[l:r+1])
        res =[]
        while r < len(nums):
            highest = max(nums[l:r+1])
            res.append(highest)
            r += 1
            l += 1
        return res