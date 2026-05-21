# it will take max(piles) to finish the fastest
# if hours taken to eat bananas  is less than h search for less rate
# if hours taken to eat bananas is more than h search for higher rate


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = max(piles)
        while l <= r:
            rate = (r+l)//2
            total= 0
            for p in piles:
                total += math.ceil(p/rate)
            if total<=h:
                r = rate-1
                res = min(rate,res)
            else:
                l = rate +1
        return res
            