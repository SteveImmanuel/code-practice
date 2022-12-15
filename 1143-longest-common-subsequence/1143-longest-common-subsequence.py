class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        mem = [[None for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    mem[i][j] = 1 if text1[i] == text2[j] else 0
                elif i == 0:
                    mem[i][j] = min(1, mem[i][j-1] + (1 if text1[i] == text2[j] else 0))
                elif j == 0:
                    mem[i][j] = min(1, mem[i-1][j] + (1 if text1[i] == text2[j] else 0))
                else:
                    if text1[i] == text2[j]:
                        mem[i][j] = 1 + mem[i-1][j-1]
                    else:
                        mem[i][j] = max(mem[i-1][j], mem[i][j-1])
        # print(mem)
        return mem[-1][-1]