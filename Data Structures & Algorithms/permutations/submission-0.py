class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]
        for n in nums:
            curr = []
            for p in perm:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i,n)
                    curr.append(pCopy)
                perm = curr
        return perm
            