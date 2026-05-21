class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for l in word:
            if l not in curr.children:
                curr.children[l] = TreeNode()
            curr = curr.children[l]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for l in word:
            if l not in curr.children:
                return False
            curr = curr.children[l]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for l in prefix:
            if l not in curr.children:
                return False
            curr = curr.children[l]
        return True
        
        