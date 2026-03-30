import gc

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        head2 = l2
        tenHolder = 1

        num1 = 0
        while head1:
            num1 += (head1.val * tenHolder)
            tenHolder *= 10
            head1 = head1.next

        head1 = None
        l1 = None

        tenHolder = 1

        num2 = 0
        while head2:
            num2 += (head2.val * tenHolder)
            tenHolder *= 10
            head2 = head2.next

        head2 = None
        l2 = None

        num1 = num1 + num2
        num2 = None

        dummy = ListNode(0)
        current = dummy

        while int(num1 / 10) != 0:
            holder = num1 % 10
            current.next = ListNode(holder)
            current = current.next
            num1 = int(num1 / 10)

        current.next = ListNode(num1)

        gc.collect()
        return dummy.next




