# https://leetcode.com/problems/fibonacci-number/
from typing import List

class Solution:
    def fib(self, n: int) -> int:
        mem = [None] * (n+1)
        mem[0] = 0
        if len(mem) >= 2:  
            mem[1] = 1
        # print(n, mem)
        for i in range(2, n+1):
            # print(i)
            mem[i] = mem[i-1] + mem[i-2]
        
        return mem[n]
        
sol = Solution()
for i in range(10):
    print(sol.fib(i))