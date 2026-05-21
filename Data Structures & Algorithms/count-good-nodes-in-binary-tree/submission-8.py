# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,highest):
            if not root:
                return 0
            res = 1 if highest<= root.val else 0
            highest = max(highest,root.val)
            res += dfs(root.left,highest)
            res += dfs(root.right,highest)
            return res
        return dfs(root,root.val)