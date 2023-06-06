"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.construct_rec(0, 0, n-1, n-1, grid)
        
    def construct_rec(self, i, j, k, l, grid):
        if i == k:
            return Node(grid[i][j], 1, None, None, None, None)
        else:
            val = grid[i][j]
            same = True
            for it in range(i, k+1):
                for jt in range(j, l+1):
                    if grid[it][jt] != val:
                        same = False
                        break
            if same:
                return Node(val, 1, None, None, None, None)
            else:
                half = (k - i + 1) // 2
                head = Node(1, 0, None, None, None, None)
                head.topLeft = self.construct_rec(i, j, k - half, l - half, grid)
                head.topRight = self.construct_rec(i, j + half, k - half, l, grid)                
                head.bottomLeft = self.construct_rec(i + half, j, k, l - half, grid)                
                head.bottomRight = self.construct_rec(i + half, j + half, k, l, grid)
                return head