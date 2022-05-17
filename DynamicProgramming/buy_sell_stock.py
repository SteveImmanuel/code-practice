# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_arr = [None] * len(prices)
        min_arr = [None] * len(prices)
        cur_max = None
        cur_min = None

        for i in range(len(prices) - 1, -1, -1):
            if cur_max is None or prices[i] > cur_max:
                cur_max = prices[i]
            max_arr[i] = cur_max
        
        for i in range(len(prices)):
            if cur_min is None or prices[i] < cur_min:
                cur_min = prices[i]
            min_arr[i] = cur_min

        profit = None
        for i in range(len(prices)):
            temp = max_arr[i] - min_arr[i]
            if profit is None or temp > profit:
                profit = temp

        return max(0, profit)
        
        # cur_min_idx = 0
        # cur_max_idx = 0
        # prices.append(0)

        # for i in range(1, len(prices) - 1):
        #     # print(i)
        #     print(i, prices[i] < prices[i - 1], prices[i] < prices[cur_min_idx])
        #     if prices[i] < prices[i - 1] and prices[i] < prices[cur_min_idx]:
        #         cur_min_idx = i
        #         cur_max_idx = i
            
        #     if prices[i] > prices[i + 1] and prices[i] > prices[cur_max_idx] and i > cur_min_idx:
        #         cur_max_idx = i
        # print(cur_min_idx, cur_max_idx)
        # return prices[cur_max_idx] - prices[cur_min_idx]

sol = Solution()
prices = [2,4,1]
print(sol.maxProfit(prices))