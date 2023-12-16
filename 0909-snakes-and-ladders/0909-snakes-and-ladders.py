class Solution:
    def unwrap_board(self, board):
        board_list = []
        n = len(board)
        odd = True
        for i in range(n-1, -1, -1):
            if odd:
                start_idx = 0
                end_idx = n
                step = 1
            else:
                start_idx = n - 1
                end_idx = -1
                step = -1
            for j in range(start_idx, end_idx, step):
                board_list.append(board[i][j])
            odd = not odd
        return board_list
    
    def print_idx(self, x):
        t = [(i+1, z) for i, z in enumerate(x)]
        print(t)
        print()
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        uboard = self.unwrap_board(board)
        # self.print_idx(uboard)
        res = [None] * len(uboard)
        # print('start')
        change = 3
        while change > 0:
            
            # change = False
            for i in range(len(uboard) - 1, -1, -1):
                if i == len(uboard) - 1:
                    res[i] = 0
                else:
                    shortest = float('inf')
                    for j in range(i + 1, min(i + 7, len(uboard))):
                        if uboard[j] == -1:
                            if res[j] != -1 and res[j] < shortest:
                                shortest = res[j]
                        elif uboard[j] > j + 1:
                            if res[uboard[j] - 1] != -1 and res[uboard[j] - 1] < shortest:
                                shortest = res[uboard[j] - 1]
                    
                    if res[i] is None or res[i] == -1 or res[i] > shortest + 1:
                        if shortest == float('inf'):
                            res[i] = -1
                        else:
                            res[i] = shortest + 1
                        # change = True
                    # res[i] = 1 + shortest

            # self.print_idx(res)

            for i in range(len(uboard)):
                shortest = float('inf')
                for j in range(i + 1, min(i + 7, len(uboard))):
                    if uboard[j] != -1 and uboard[j] < j + 1:
                        if res[uboard[j] - 1] != -1 and res[uboard[j] - 1] < shortest:
                            shortest = res[uboard[j] - 1]
                #     print(i+1, uboard[j], shortest)
                # print(i+1, shortest)
                # print()
                
                
                if res[i] is None or res[i] == -1 or res[i] > shortest + 1:
                        if shortest == float('inf'):
                            res[i] = -1
                        else:
                            res[i] = shortest + 1
                        # change = True
                # res[i] = min(res[i], 1 + shortest)

            # self.print_idx(res)
            change -= 1
        
        return res[0]
        