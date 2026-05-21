class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = []
        for i in nums:
            if i in array:
                return True
            else: array.append(i)
        return False
         