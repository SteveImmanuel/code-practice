class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        mem = [None] * len(cost)
        
        for i in range(len(cost)):
            if i == 0 or i == 1:
                mem[i] = 0
            else:
                mem[i] = min(mem[i-2] + cost[i-2], mem[i-1] + cost[i-1])
        
        return mem[-1]