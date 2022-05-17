# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_min = prices[0]
        prices.append(0)
        is_going_up = prices[0] < prices[1]

        for i in range(1, len(prices) - 1):
            if prices[i] < prices[i + 1] and not is_going_up:
                is_going_up = True
                cur_min = prices[i]
            elif prices[i] > prices[i + 1] and is_going_up:
                is_going_up = False
                profit += prices[i] - cur_min
                cur_min = prices[i + 1]
            elif prices[i] > prices[i + 1] and not is_going_up:
                cur_min = prices[i + 1]
        
        return profit

sol = Solution()
prices = [1,2,3,4,5]
print(sol.maxProfit(prices))