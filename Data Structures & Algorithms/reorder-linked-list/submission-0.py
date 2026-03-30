# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Always keep track of pointers!
        slow = head
        fast = head
        start = head

        # Boilerplate for finding midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Boilerplate for linked list reversal

        second = slow.next
        slow.next = None
        curr = second

        prev = None
        while curr:
            next_holder = curr.next
            curr.next = prev
            prev = curr
            curr = next_holder

        first = head
        second = prev

        # Boilerplate for merging lists
        

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2



