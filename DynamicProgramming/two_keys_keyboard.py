# https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    def minSteps(self, n: int) -> int:
        memory = [None] * n

        for i in range(n):
            if i == 0:
                memory[i] = 0
            else:
                if i % 2 == 0:
                    biggest_factor = self.biggestFactor(i + 1)
                    if biggest_factor == -1:
                        memory[i] = i + 1
                    else:
                        memory[i] = memory[biggest_factor-1] + (i + 1) // biggest_factor
                else:
                    memory[i] = memory[(i-1)//2] + 2
        return memory[n-1]

    def biggestFactor(self, n):
        for i in range(2, int(n**.5) + 1):
            if n % i == 0:
                return n // i
        return -1

sol = Solution()
n = 10
print(sol.minSteps(n))