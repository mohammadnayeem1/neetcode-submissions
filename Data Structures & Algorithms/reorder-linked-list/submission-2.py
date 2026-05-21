# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = slow.next
        slow.next = None
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        first = head
        second = prev
        while second:
            tmp1 ,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


