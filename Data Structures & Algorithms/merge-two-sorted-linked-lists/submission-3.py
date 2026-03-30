import gc

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        all_values = []

        head1 = list1
        head2 = list2

        while head1:
            all_values.append(head1.val)
            head1 = head1.next

        while head2:
            all_values.append(head2.val)
            head2 = head2.next

        all_values.sort()


        dummy = ListNode(0)
        current = dummy

        for node in all_values:
            current.next = ListNode(node)
            current = current.next

        list1 = None
        list2 = None
        head1 = None
        head2 = None
        all_values = None

        gc.collect()

        return dummy.next




