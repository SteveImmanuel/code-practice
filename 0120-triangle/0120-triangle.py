class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mem = []
        
        for i in range(len(triangle)):
            if i == 0:
                mem.append([triangle[i][0]])
            else:
                row_mem = []
                for j in range(len(triangle[i])):
                    if j == 0:
                        prev_min_sum = mem[i - 1][j]
                    elif j == len(triangle[i]) - 1:
                        prev_min_sum = mem[i - 1][j - 1]
                    else:
                        prev_min_sum = min(mem[i - 1][j - 1], mem[i - 1][j])
                    row_mem.append(triangle[i][j] + prev_min_sum)
                mem.append(row_mem)
        return min(mem[-1])