class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # O(k)

    # Step 2: Iterate through the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:  # Only replace if current number is larger than the smallest in the heap
                heapq.heapreplace(min_heap, num)  # O(log k)

    # Step 3: The root of the min-heap is the k-th largest element
        return min_heap[0]
