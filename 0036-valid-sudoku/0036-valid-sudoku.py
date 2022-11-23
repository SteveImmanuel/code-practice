class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horizontal
        for i in range(9):
            checker = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in checker:
                    return False
                else:
                    checker.add(board[i][j])
        
        #vertical
        for i in range(9):
            checker = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in checker:
                    return False
                else:
                    checker.add(board[j][i])

        init_pos = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for pos in init_pos:
            checker = set()
            for i in range(3):
                for j in range(3):
                    if board[pos[0] + i][pos[1] + j] != '.' and board[pos[0] + i][pos[1] + j] in checker:
                        return False
                    else:
                        checker.add(board[pos[0] + i][pos[1] + j])
        return True