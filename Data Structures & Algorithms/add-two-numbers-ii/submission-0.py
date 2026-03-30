# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        


        prev = None
        current = l1

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        invl1 = prev

        prev = None
        current = l2


        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        invl2 = prev


# After reversal, to print all nodes in invL2:
        current = invl1
        sf = 1
        num1 = 0
        
        while current:
            num1 += current.val * sf
            sf *= 10
            current = current.next

        current = invl2
        sf = 1
        num2 = 0
        while current:    
            num2 += current.val * sf
            sf *= 10
            current = current.next

        summed = num1 + num2

        summed = str(summed)

        dummy = ListNode(0)
        current = dummy
        for c in summed:
            current.next = ListNode(int(c))
            current = current.next


        return dummy.next


        











