class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        mem = [[None for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
                if j == 0:
                    mem[i][j] = 1
                elif i == 0:
                    mem[i][j] = 0
                else:
                    if s[i-1] == t[j-1]:
                        mem[i][j] = mem[i-1][j] + mem[i-1][j-1]
                    else:
                        mem[i][j] = mem[i-1][j]
            # print(mem)
            # print()
        return mem[n][m]
                