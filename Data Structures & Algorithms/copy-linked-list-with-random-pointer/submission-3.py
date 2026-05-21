"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {None:None}
        curr = head
        while curr:
            newNode = Node(curr.val)
            hm[curr] = newNode
            curr = curr.next
        curr = head
        while curr:
            node = hm[curr]
            node.next = hm[curr.next]
            node.random = hm[curr.random]
            curr= curr.next
        return hm[head]