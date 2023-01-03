class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        mem = [[None for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    mem[i][j] = 0
                elif i == 0:
                    mem[i][j] = j
                elif j == 0:
                    mem[i][j] = i
                else:
                    if word1[j-1] == word2[i-1]:
                        mem[i][j] = mem[i-1][j-1]
                    else:
                        mem[i][j] = 1 + min(mem[i-1][j-1], mem[i-1][j], mem[i][j-1])
        
        return mem[m][n]