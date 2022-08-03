# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.climb(cost), self.climb(cost[1:]))

    def climb(self, cost):
        mem = [None] * len(cost)
        for i in range(len(mem)):
            if i == 0:
                mem[i] = cost[i]
            elif i == 1:
                mem[i] = cost[i] + mem[i-1]
            else:
                mem[i] = cost[i] + min(mem[i-1], mem[i-2])
        if len(mem) > 1:
            return min(mem[-1], mem[-2])
        return mem[-1]

sol = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]
cost = [10,15,20]
print(sol.minCostClimbingStairs(cost))