# it will take max(piles) to finish the fastest
# if hours taken to eat bananas  is less than h search for less rate
# if hours taken to eat bananas is more than h search for higher rate


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = max(piles)
        while l<= r:
            mid = (l+r) //2 
            totalHours = 0
            for p in piles:
                totalHours += math.ceil(p/mid)
            if totalHours <= h:
                r = mid - 1
                res = min(res,mid)
            else:
                l = mid + 1
        return res
