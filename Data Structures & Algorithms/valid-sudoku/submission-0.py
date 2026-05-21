class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        verticalSet = defaultdict(set)
        horizontalSet= defaultdict(set)
        subSet = defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if num in verticalSet[r] or num in horizontalSet[c] or num in subSet[(r//3,c//3)]:
                    return False
                else:
                    verticalSet[r].add(num)
                    horizontalSet[c].add(num)
                    subSet[(r//3,c//3)].add(num)
        return True 