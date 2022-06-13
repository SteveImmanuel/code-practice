# https://leetcode.com/problems/n-queens-ii/
from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        return len(self.solveRec([], 0, n)) 

    def check_possible(self, pos, queens):
        for q_row, q_col in enumerate(queens):
            if q_col == pos[1]:
                return False
            if abs(pos[0] - q_row) == abs(pos[1] - q_col):
                return False
        return True

    def solveRec(self, current_queens, cur_row, n):
        res = []
        for i in range(n):
            temp_cur_queens = current_queens.copy()

            if self.check_possible((cur_row, i), temp_cur_queens):
                temp_cur_queens.append(i)

                if cur_row < n - 1:
                    res += self.solveRec(temp_cur_queens, cur_row+1, n)
                else:
                    res.append(temp_cur_queens)
                
        return res
        

sol = Solution()
n = 9
print(sol.totalNQueens(n))