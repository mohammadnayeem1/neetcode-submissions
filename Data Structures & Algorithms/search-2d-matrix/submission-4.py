class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r , c = len(matrix), len(matrix[0])
        l = 0
        r = r*c -1
        while l <= r:
            mid = (l+r)//2
            midVal = matrix[mid//c][mid%c]
            if target>midVal:
                l = mid + 1
            elif target<midVal:
                r = mid - 1
            else:
                return True
        return False