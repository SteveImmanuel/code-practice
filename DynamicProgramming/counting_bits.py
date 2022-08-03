# https://leetcode.com/problems/counting-bits/
from typing import List

class Solution:
    def closest_power_2(self, n):
        val = 1
        while n > 1:
            val *= 2
            n //= 2
        return val

    def countBits(self, n: int) -> List[int]:
        mem = {0:0}
        for i in range(n+1):
            self.counting_bits_rec(i, mem)
        return list(mem.values())
    
    def counting_bits_rec(self, n, mem):
        if n not in mem:
            mem[n] = 1 + self.counting_bits_rec(n - self.closest_power_2(n), mem)
        return mem[n]

sol = Solution()
for i in range(10):
    print(sol.countBits(i))