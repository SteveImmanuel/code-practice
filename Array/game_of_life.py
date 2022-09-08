# https://leetcode.com/problems/game-of-life/
from re import L
from typing import List
class Solution:
    # Runtime: 18 ms, faster than 100.00% of Python3 online submissions for Game of Life.
    # Memory Usage: 13.8 MB, less than 91.37% of Python3 online submissions for Game of Life.
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        counter_board = [[None for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                total_live = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if k < 0 or k >= len(board) or l < 0 or l >= len(board[i]) or (k==i and l==j):
                            continue
                        if board[k][l] == 1:
                            total_live += 1
                counter_board[i][j] = total_live
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    if counter_board[i][j] > 3:
                        board[i][j] = 0
                    elif counter_board[i][j] > 1:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if counter_board[i][j] == 3:
                        board[i][j] = 1

sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(board)
print(board)
