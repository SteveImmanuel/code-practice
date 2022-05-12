# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        total = 0
        board_visit = []
        for i in range(len(board)):
            board_visit.append([])
            for j in range(len(board[i])):
                board_visit[i].append(False)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board_visit[i][j]:
                    continue

                board_visit[i][j] = True
                if board[i][j] == 'X':
                    total += 1

                    #traverse horizontal
                    k = j - 1
                    while (k >= 0) and board[i][k] == 'X' and not board_visit[i][k]:
                        board_visit[i][k] = True
                        k -= 1

                    k = j + 1
                    while (k < len(board[i])) and board[i][k] == 'X' and not board_visit[i][k]:
                        board_visit[i][k] = True
                        k += 1

                    #traverse vertical
                    k = i - 1
                    while (k >= 0) and board[k][j] == 'X' and not board_visit[k][j]:
                        board_visit[k][j] = True
                        k -= 1

                    k = i + 1
                    while (k < len(board)) and board[k][j] == 'X' and not board_visit[k][j]:
                        board_visit[k][j] = True
                        k += 1
                    

        return total

sol = Solution()
board = [["X",'X', 'X']]
print(sol.countBattleships(board))