# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Boilerplate for finding midpoint

        slow = head # Initialize slow
        fast = head # Initialize fast
        while fast and fast.next: # Note, left list larger on odd node counts
            slow = slow.next # Push slow forward by one space
            fast = fast.next.next # Push fast forward by two 

        # Boilerplate for linked list reversal

        second = slow.next # These two lines break the list
        slow.next = None   # These two lines break the list

        curr = second # curr = second = slow.next, the second half

        prev = None # This is the new "final" node of the list
        while curr: # Traverse through the list

            next_holder = curr.next # First, hold the true "next"
            curr.next = prev # Next, redirect the arrow/next to the last node
            prev = curr # Setup next loop, set last node to be the current one
            curr = next_holder # Current node is the next one



        # Boilerplate for merging lists
        
        first = head # Assign the sm
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2




