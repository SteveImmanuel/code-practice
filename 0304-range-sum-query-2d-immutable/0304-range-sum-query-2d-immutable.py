class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.matrix = [[None for _ in range(m)] for _ in range(n)]
        for i in range(n):
            cur_row_sum = 0
            for j in range(m):
                cur_row_sum += matrix[i][j]
                if i == 0:
                    self.matrix[i][j] = cur_row_sum
                else:
                    self.matrix[i][j] = cur_row_sum + self.matrix[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.matrix[row2][col2]
        if row1 > 0:
            total -= self.matrix[row1 - 1][col2]
        if col1 > 0:
            total -= self.matrix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            total += self.matrix[row1 - 1][col1 - 1]
        return total
        
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)