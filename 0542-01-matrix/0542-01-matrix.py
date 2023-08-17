class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result_mat = [[None for _ in range(n)] for _ in range(m)]
        queue = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(queue) > 0:
            i, j, val = queue.pop(0)
            if i >= m or i < 0 or j >= n or j < 0 or result_mat[i][j] is not None:
                continue
                
            result_mat[i][j] = val
            for dir in dirs:
                queue.append((i+dir[0], j+dir[1], val+1))

        
        return result_mat