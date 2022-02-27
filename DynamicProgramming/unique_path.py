# https://leetcode.com/problems/unique-paths/

class Solution:
    def factorial(self, n, mem):
        if n in mem:
            return mem[n]

        for i in range(2,n+1):
            if i not in mem:
                mem[i] = i * mem[i-1]
            
        return mem[n]


    def uniquePaths(self, m: int, n: int) -> int:
        mem = {0:1,1:1}
        return self.factorial(m+n-2,mem) // (self.factorial(m-1,mem) * self.factorial(n-1,mem)) 

sol = Solution()
m=3
n=7
print(sol.uniquePaths(m,n))
