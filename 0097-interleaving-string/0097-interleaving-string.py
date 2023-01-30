class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1) + len(s2)):
            return False
        
        n = len(s1)
        m = len(s2)
        mem = [[None for _ in range(n+1)] for _ in range(m+1)]
        
        
        for i in range(m+1):
            for j in range(n+1):
                cur_idx = i + j - 1
                if i == 0 and j == 0:
                    mem[i][j] = True
                elif i == 0:
                    mem[i][j] = mem[i][j-1] and s1[j-1] == s3[cur_idx]
                elif j == 0:
                    mem[i][j] = mem[i-1][j] and s2[i-1] == s3[cur_idx]
                else:
                    mem[i][j] = (mem[i][j-1] and s1[j-1] == s3[cur_idx]) or (mem[i-1][j] and s2[i-1] == s3[cur_idx])
        
        # for a in mem:
        #     print(a)
        
        return mem[m][n]