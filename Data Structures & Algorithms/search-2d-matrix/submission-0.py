class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l<=r:
            mid = (l+r)//2
            leftVal = matrix[mid][0]
            rightVal = matrix[mid][-1]
            if target in matrix[mid]:
                return True
            elif target<leftVal:
                r = mid - 1
            else:
                l = mid + 1
        return False        