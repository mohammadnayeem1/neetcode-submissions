class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap,num*-1)
        for _ in range(k-1):
            heapq.heappop(maxHeap)
        return maxHeap[0]*-1
