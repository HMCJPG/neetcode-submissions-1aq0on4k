# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root
        a = p.val
        b = q.val

        while curr:
            c = curr.val

            if c > a and c > b:
                curr = curr.left
            elif c < a and c < b:
                curr = curr.right
            else:
                return curr