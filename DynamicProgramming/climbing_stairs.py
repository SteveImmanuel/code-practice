# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairsRec(n, {})
    
    def climbStairsRec(self, n, mem):
        if n not in mem:
            if n <= 1:
                mem[n] = 1
            else:
                mem[n] = self.climbStairsRec(n - 1, mem) + self.climbStairsRec(n - 2, mem)
        return mem[n]
    

sol = Solution()
print(sol.climbStairs(35))