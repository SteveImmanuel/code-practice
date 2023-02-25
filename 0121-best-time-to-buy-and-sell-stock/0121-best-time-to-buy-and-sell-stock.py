class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_arr = [None] * len(prices)
        cur_max = None

        for i in range(len(prices) - 1, -1, -1):
            if cur_max is None or prices[i] > cur_max:
                cur_max = prices[i]
            max_arr[i] = cur_max
        
        profit = None
        for i in range(len(prices)):
            if profit is None or max_arr[i] - prices[i] > profit:
                profit = max_arr[i] - prices[i]

        return max(0, profit)