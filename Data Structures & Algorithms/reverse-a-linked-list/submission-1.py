# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode(0)

        prev = None
        current = head

        while current:
            origNext = current.next
            current.next = prev
            prev = current
            current = origNext

        return prev
            