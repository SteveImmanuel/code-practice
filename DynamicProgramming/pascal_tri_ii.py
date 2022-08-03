# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tree = [None] * (rowIndex+1)
        tree[0] = [1]
        if rowIndex >= 1:
            tree[1] = [1, 1]
            for i in range(2, rowIndex+1):
                res = []
                for j in range(0, len(tree[i-1]) - 1):
                    res.append(tree[i-1][j]+tree[i-1][j+1])
                tree[i] = res
                tree[i] = [1] + tree[i] + [1]
        return tree[-1]

sol = Solution()
print(sol.getRow(1))