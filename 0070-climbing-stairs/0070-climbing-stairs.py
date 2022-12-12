class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [None] * n
        
        for i in range(n):
            if i == 0:
                mem[i] = 1
            elif i == 1:
                mem[i] = 2
            else:
                mem[i] = mem[i-1] + mem[i-2]
        
        return mem[-1]