# https://leetcode.com/problems/minimum-cost-for-tickets/
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        min_cost = [None] * len(days)
        for i in range(len(days)):
            for j in range(len(costs)):
                current_day = days[i]
                temp_cost = costs[j]
                if i != 0:
                    temp_cost += min_cost[i-1]
                
                if j == 0:
                    last_day = current_day

                elif j == 1:
                    last_day = current_day + 6

                elif j == 2:
                    last_day = current_day + 29

                k = self.find_last_idx(i, last_day, days)
                if min_cost[k] is None or min_cost[k] > temp_cost:
                    min_cost[k] = temp_cost
        
        return min_cost[-1]

    def find_last_idx(self, current_idx, last_day, days):
        k = current_idx + 1
        while k < len(days) and days[k] <= last_day:
            k += 1
        k -= 1

        return k

sol = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(sol.mincostTickets(days, costs))