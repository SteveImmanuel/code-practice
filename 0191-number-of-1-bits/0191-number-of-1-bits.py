class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n > 0:
            total += n & 1
            n = n >> 1
        return total