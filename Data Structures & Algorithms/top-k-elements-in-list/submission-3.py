class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num,0)
        heap =[]
        for key,value in hm.items():
            heapq.heappush(heap,(value,key))
            while len(heap)>k:
                heapq.heappop(heap)
        return [num for _,num in heap]