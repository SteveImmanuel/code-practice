class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        start_coordinate = [(i, 0) for i in range(m-1, -1, -1)] + [(0, i) for i in range(1, n)]
        # print(start_coordinate)
        for coordinate in start_coordinate:
            cur_x, cur_y = coordinate
            value = matrix[cur_x][cur_y]
            
            while True:
                cur_x += 1
                cur_y += 1
                if cur_x >= m or cur_y >= n:
                    break
                
                if matrix[cur_x][cur_y] != value:
                    return False
        
        return True
                    