# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        arr = []

        def inorder(Node):

            if not Node:
                return
            inorder(Node.left)
            arr.append(Node.val)
            inorder(Node.right)

        inorder(root)

        return arr[k-1]