class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for key,val in c.items():
            heapq.heappush(heap,[-val,key])
        return [heapq.heappop(heap)[1] for _ in range(k)]