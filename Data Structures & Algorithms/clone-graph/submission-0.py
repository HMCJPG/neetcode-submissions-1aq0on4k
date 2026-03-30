"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        old2new : dict[Node, Node] = {}

        def dfs(orig: 'Node') -> 'Node':
            if orig is None:
                return None

            if orig in old2new:
                return old2new[orig]

            copy = Node(orig.val)
            old2new[orig] = copy

            for n in orig.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node)
