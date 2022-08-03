# https://leetcode.com/problems/pascals-triangle/
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tree = [None] * numRows
        tree[0] = [1]
        if numRows > 1:
            tree[1] = [1, 1]
            for i in range(2, numRows):
                res = []
                for j in range(0, len(tree[i-1]) - 1):
                    res.append(tree[i-1][j]+tree[i-1][j+1])
                tree[i] = res
                tree[i] = [1] + tree[i] + [1]
        return tree

sol = Solution()
print(sol.generate(5))