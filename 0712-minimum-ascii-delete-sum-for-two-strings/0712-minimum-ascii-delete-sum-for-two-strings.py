class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        mem = [[None for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        for i in range(len(s2) + 1):
            for j in range(len(s1) + 1):
                if i == 0:
                    if j == 0:
                        mem[i][j] = 0
                    else:
                        mem[i][j] = mem[i][j - 1] + ord(s1[j - 1])
                elif j == 0:
                    if i == 0:
                        mem[i][j] = 0
                    else:
                        mem[i][j] = mem[i - 1][j] + ord(s2[i - 1])
                else:
                    if s1[j-1] == s2[i-1]:
                        mem[i][j] = mem[i - 1][j - 1]
                    else:
                        mem[i][j] = min(ord(s2[i - 1]) + mem[i - 1][j], ord(s1[j - 1]) + mem[i][j - 1])
        return mem[len(s2)][len(s1)]