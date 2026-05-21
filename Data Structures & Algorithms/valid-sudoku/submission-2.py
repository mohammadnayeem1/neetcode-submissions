class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmR = defaultdict(set)
        hmC = defaultdict(set)
        hmS = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in hmR[r] or board[r][c] in hmC[c] or board[r][c] in hmS[r//3,c//3]):
                    return False
                else:
                    hmR[r].add(board[r][c])
                    hmC[c].add(board[r][c])
                    hmS[r//3,c//3].add(board[r][c])
        return True