# https://leetcode.com/problems/surrounded-regions/

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visitation_mat = []
        for i in range(len(board)):
            visitation_mat.append([False] * len(board[i]))

        max_row = len(board) - 1
        max_col = len(board[0]) - 1

        for i in range(len(board)):
            for j in range(len(board[i])):
                if i in [0, max_row] or j in [0, max_col]:
                    if board[i][j] == 'O':
                        self.DFS(i, j, board, visitation_mat)
        
        for i in range(1, len(board)):
            for j in range(1, len(board[i])):
                if board[i][j] == 'O' and not visitation_mat[i][j]:
                    board[i][j] = 'X'

    def DFS(self, cur_row, cur_col, board, visitation_mat):
        if visitation_mat[cur_row][cur_col]:
            return

        visitation_mat[cur_row][cur_col] = True

        if cur_row > 0:
            if board[cur_row-1][cur_col] == 'O' and not visitation_mat[cur_row-1][cur_col]:
                self.DFS(cur_row-1, cur_col, board, visitation_mat)
        if cur_row < (len(board) - 1):
            if board[cur_row+1][cur_col] == 'O' and not visitation_mat[cur_row+1][cur_col]:
                self.DFS(cur_row+1, cur_col, board, visitation_mat)
        if cur_col > 0:
            if board[cur_row][cur_col-1] == 'O' and not visitation_mat[cur_row][cur_col-1]:
                self.DFS(cur_row, cur_col-1, board, visitation_mat)
        if cur_col < (len(board[0]) - 1):
            if board[cur_row][cur_col+1] == 'O' and not visitation_mat[cur_row][cur_col+1]:
                self.DFS(cur_row, cur_col+1, board, visitation_mat)


sol = Solution()       
board = [["O","O"],["O","O"]]
sol.solve(board)

for a in board:
    print(a)