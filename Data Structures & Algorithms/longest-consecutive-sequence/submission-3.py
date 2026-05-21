class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()
        res = 0
        for num in nums:
            if num-1 not in hs:
                length = 1
                while num + length in nums:
                    hs.add(num+length)
                    length += 1
                res = max(res,length)
        return res