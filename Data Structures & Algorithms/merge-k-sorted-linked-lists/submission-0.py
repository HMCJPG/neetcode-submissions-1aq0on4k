# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        all_nodes = []

        for head in lists:
            while head:
                all_nodes.append(head.val)
                head = head.next

        all_nodes.sort()


        dummy = ListNode(0)
        current = dummy
        
        for item in all_nodes:
            current.next = ListNode(item)
            current = current.next

        return dummy.next






