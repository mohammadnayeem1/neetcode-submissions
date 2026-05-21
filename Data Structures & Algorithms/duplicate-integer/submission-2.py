class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for val in c.values():
            if val >1:
                return True
        return False