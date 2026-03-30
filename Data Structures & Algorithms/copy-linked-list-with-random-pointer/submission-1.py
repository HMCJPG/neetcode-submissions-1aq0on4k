"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        o2n = {}

        current = head
        while current:
            o2n[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            clone = o2n[current]
            clone.next = o2n.get(current.next)
            clone.random = o2n.get(current.random)
            current = current.next

        return o2n[head]