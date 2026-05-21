class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            goal = target - num
            if goal in hm:
                return [hm[goal],i]
            else:
                hm[num] = i
        return []