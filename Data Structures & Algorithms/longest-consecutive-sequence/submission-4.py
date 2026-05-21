class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numS = set(nums)
        res = 0
        for num in nums:
            if  num - 1 not in numS:
                streak = 0
                while num + streak in numS:
                    streak += 1
                res = max(res,streak)
        return res