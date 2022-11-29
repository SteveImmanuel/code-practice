class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        memory = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(15):
            for i in range(n):
                for j in range(m):
                    if i==0 and j==0:
                        memory[i][j] = max(memory[i][j], 1)
                    else:
                        possible = 1
                        if i==0:
                            if matrix[i][j] < matrix[i][j-1]:
                                possible += memory[i][j-1]
                        elif j==0:
                            if matrix[i][j] < matrix[i-1][j]:
                                possible += memory[i-1][j]
                        else:
                            max_add = 0
                            if matrix[i][j] < matrix[i][j-1]:
                                max_add = max(max_add, memory[i][j-1])
                            if matrix[i][j] < matrix[i-1][j]:
                                max_add = max(max_add, memory[i-1][j])
                            possible += max_add
                        memory[i][j] = max(memory[i][j], possible)

            # for a in memory:
            #     print(a)

            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    if i==n-1 and j==m-1:
                        memory[i][j] = max(memory[i][j], 1)
                    else:
                        possible = 1
                        if i==n-1:
                            if matrix[i][j] < matrix[i][j+1]:
                                possible += memory[i][j+1]
                        elif j==m-1:
                            if matrix[i][j] < matrix[i+1][j]:
                                possible += memory[i+1][j]
                        else:
                            max_add = 0
                            if matrix[i][j] < matrix[i][j+1]:
                                max_add = max(max_add, memory[i][j+1])
                            if matrix[i][j] < matrix[i+1][j]:
                                max_add = max(max_add, memory[i+1][j])
                            possible += max_add
                        memory[i][j] = max(memory[i][j], possible)

            # for a in memory:
            #     print(a)
        
        max_length = 0
        for i in range(n):
            for j in range(m):
                max_length = max(max_length, memory[i][j])
        return max_length
        
        