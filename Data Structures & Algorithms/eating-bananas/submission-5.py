class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #[1,2,3,4]
        #4 - 4 hours, 4 < 9 move right to 3 
        #3 - 5 hours, 5< 9 move right to 2
        #2 - 6 hours 
        res =  r = max(piles)
        l = 1
        while l <= r:
            rate = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/rate)
            if hours <= h:
                r = rate - 1
                res = min(res,rate)
            else:
                l = rate + 1
        return res