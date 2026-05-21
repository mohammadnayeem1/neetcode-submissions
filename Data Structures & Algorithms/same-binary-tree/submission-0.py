# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pRes = []
        qRes = []
        def dfs(root,res):
            if not root:
                return res.append(None)
            dfs(root.left,res)
            dfs(root.right,res)
            res.append(root.val)
        dfs(p,pRes)
        dfs(q,qRes)
        print(pRes,qRes)
        return pRes == qRes