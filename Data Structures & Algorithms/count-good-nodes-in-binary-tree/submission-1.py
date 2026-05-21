# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()
        if root:
            q.append((root,root.val))
        while len(q) > 0 :
            for r in range(len(q)):
                root,maxVal = q.popleft()
                if root.val >= maxVal:
                    res += 1
                maxVal = max(maxVal, root.val)
                if root.left:
                    q.append((root.left,maxVal))
                if root.right:
                    q.append((root.right,maxVal))
        return res