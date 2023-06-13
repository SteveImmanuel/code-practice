class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = []
        n = len(grid)
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            cols.append(col)
            
        row_dict = defaultdict(int)
        for row in grid:
            row_dict[tuple(row)] += 1
        col_dict = defaultdict(int)
        for row in cols:
            col_dict[tuple(row)] += 1
        
        total = 0
        for key in row_dict:
            if key in col_dict:
                total += row_dict[key] * col_dict[key]
        
        return total
        
        