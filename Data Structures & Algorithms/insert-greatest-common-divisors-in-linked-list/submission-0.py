# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a, b):
            while b > 0:
                remainder = a % b
                a = b
                b = remainder

            return a

        current = head

        while current and current.next:

            val1 = current.val
            val2 = current.next.val

            gcd_value = gcd(val1, val2)
            new_node = ListNode(gcd_value)

            new_node.next = current.next
            current.next = new_node

            current = current.next.next

        return head


