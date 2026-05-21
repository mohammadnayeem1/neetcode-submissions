class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:
            distance = (x*x) + (y*y)
            minheap.append([distance,x,y])
        heapq.heapify(minheap)
        res = heapq.nsmallest(k,minheap)
        return [ [x,y] for _,x,y in res[:k]]