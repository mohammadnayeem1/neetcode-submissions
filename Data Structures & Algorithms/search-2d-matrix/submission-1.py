class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n= len(matrix),len(matrix[0])
        l,r = 0, m*n-1
        while l <= r:
            mid = (l + r) // 2
            midVal = matrix[mid // n][mid % n] 
            if target < midVal:
                r = mid -1
            elif target > midVal:
                l = mid + 1
            else:
                return True
        return False
                
