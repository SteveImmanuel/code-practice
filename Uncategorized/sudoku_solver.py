# https://leetcode.com/problems/sudoku-solver/

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        possibility_hor = [set([str(i) for i in range(1, 10)]) for _ in range(9)]
        possibility_ver = [set(str(i) for i in range(1, 10)) for _ in range(9)]
        possibility_block = [[set(str(i) for i in range(1, 10)) for _ in range(3)] for _ in range(3)]
        missing_indices = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    possibility_hor[i].remove(board[i][j])
                    possibility_ver[j].remove(board[i][j])
                    possibility_block[i//3][j//3].remove(board[i][j])
                else:
                    missing_indices.append((i,j))
    
        nodes = [[None for _ in range(9)] for _ in range(9)]
        
        for i,j in missing_indices:
            if board[i][j] == '.':
                nodes[i][j] = possibility_hor[i].intersection(possibility_ver[j]).intersection(possibility_block[i//3][j//3])

        self.DFS(board, nodes, missing_indices, possibility_hor, possibility_ver, possibility_block)

    def update_nodes(self, missing_indices, nodes, possibility_hor, possibility_ver, possibility_block):
        for i, j in missing_indices:
            nodes[i][j] = possibility_hor[i].intersection(possibility_ver[j]).intersection(possibility_block[i//3][j//3])

    def DFS(self, board, nodes, missing_indices, possibility_hor, possibility_ver, possibility_block):
        if len(missing_indices) == 0:
            return True
        
        index = missing_indices.pop(0)
        possible_values = nodes[index[0]][index[1]]
        if len(possible_values) == 0:
            missing_indices.insert(0, index)
            return False

        for value in possible_values:
            board[index[0]][index[1]] = value
            possibility_hor[index[0]].remove(value)
            possibility_ver[index[1]].remove(value)
            possibility_block[index[0]//3][index[1]//3].remove(value)
            self.update_nodes(missing_indices, nodes, possibility_hor, possibility_ver, possibility_block)

            if self.DFS(board, nodes, missing_indices, possibility_hor, possibility_ver, possibility_block):
                return True

            board[index[0]][index[1]] = '.'
            possibility_hor[index[0]].add(value)
            possibility_ver[index[1]].add(value)
            possibility_block[index[0]//3][index[1]//3].add(value)
            self.update_nodes(missing_indices, nodes, possibility_hor, possibility_ver, possibility_block)
        
        missing_indices.insert(0, index)
        return False




sol = Solution()
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board = [["4",".",".",".",".",".",".","1","."],[".",".",".","4",".","2","3",".","."],["8","3","6",".","1",".",".",".","."],["2",".",".",".","6",".",".","5","7"],[".","9",".","5",".",".","6",".","1"],[".",".","7","1",".",".",".",".","."],[".",".",".",".","8","6",".",".","3"],["7",".",".",".",".",".",".",".","."],["6","4",".",".","7",".",".",".","2"]]
sol.solveSudoku(board)
for row in board:
    print(row)



