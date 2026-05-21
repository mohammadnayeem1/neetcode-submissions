class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x,y in points:
            distance = x*x+y*y
            minHeap.append((distance,x,y))
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            distance,x,y = heapq.heappop(minHeap)
            res.append((x,y))
        return res



        