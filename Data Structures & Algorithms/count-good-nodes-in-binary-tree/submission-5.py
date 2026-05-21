# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        res = 0
        if root:
            q.append((root,root.val))
        while q:
            for i in range(len(q)):
                root,maxVal = q.popleft()
                if root.val>= maxVal:
                    res += 1
                maxVal = max(root.val,maxVal)
                if root.left:
                    q.append((root.left,maxVal))
                if root.right:
                    q.append((root.right,maxVal))
        return res
