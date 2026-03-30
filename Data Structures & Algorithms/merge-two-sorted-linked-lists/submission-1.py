# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not isinstance(list1, ListNode):
            if not isinstance(list2, ListNode):
                return None
            return list2
        if not isinstance(list2, ListNode):
            return list1

        merged = ListNode(0)

        head1 = list1
        head2 = list2
        tail = merged

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
                tail = tail.next
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next

        
        while head1:
            tail.next = head1
            head1 = head1.next
            tail = tail.next

        while head2:
            tail.next = head2
            head2 = head2.next
            tail = tail.next

        return merged.next
        