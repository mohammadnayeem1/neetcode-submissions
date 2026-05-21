class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums)//2
                left = nums[:mid]
                right = nums[mid:]
                mergeSort(left)
                mergeSort(right)
                
                i = j = k = 0

                while j < len(left) and k< len(right):
                    if left[j] < right[k]:
                        nums[i] = left[j]
                        j += 1
                    else:
                        nums[i] = right[k]
                        k += 1
                    i += 1
                
                while j <len(left):
                    nums[i] = left[j]
                    j += 1
                    i += 1
                while k <len(right):
                    nums[i] = right[k]
                    k += 1
                    i += 1


            return nums
        nums = mergeSort(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
