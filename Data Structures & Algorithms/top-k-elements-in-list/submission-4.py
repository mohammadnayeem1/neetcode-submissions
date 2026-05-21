class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num,0) + 1
        heap = []
        for key,val in hm.items():
             heapq.heappush(heap,(val,key))
             if len(heap) > k:
                heapq.heappop(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]
        