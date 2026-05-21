class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self,word):
        curr = self
        for l in word:
            if l not in curr.children:
                curr.children[l] = Trie()
            curr = curr.children[l]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.addWord(word)

        row, col = len(board),len(board[0])
        res,seen = set(), set()

        def dfs(r,c,node,word):
            if min(r,c) < 0 or r == row or c == col or (r,c) in seen or board[r][c] not in node.children:
                return
            seen.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            seen.remove((r,c))
        for r in range(row):
            for c in range(col):
                curr = root
                dfs(r,c,root,"")
        return list(res)