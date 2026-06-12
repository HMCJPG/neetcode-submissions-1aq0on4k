class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        leafNodes = {
            0: Node(False, True),
            1: Node(True, True)
        }

        def dfs(n, r, c):
            if n == 1:
                return leafNodes[grid[r][c]]

            n //= 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            if (topLeft.isLeaf and topRight.isLeaf 
                and bottomLeft.isLeaf and bottomRight.isLeaf
                and topLeft.val == topRight.val ==
                bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True)

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)