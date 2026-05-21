# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def sameTree(root,subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            return (root.val == subroot.val and sameTree(root.right,subroot.right) and sameTree(root.left,subroot.left))
        if sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
