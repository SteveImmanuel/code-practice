class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, h = max(weights), sum(weights)
        while l < h:
            m = (l + h) // 2
            total_days = self.get_days_for_capacity(weights, m)
            # print(l, h, m, total_days)
            if total_days > days:
                l = m + 1
            else:
                h = m
        return h
        
    def get_days_for_capacity(self, weights, capacity):
        total_day = 1
        cur_weight = 0
        for i in range(len(weights)):
            # print(i, cur_weight)
            if cur_weight + weights[i] > capacity:
                total_day += 1
                cur_weight = weights[i]
            else:
                cur_weight += weights[i]
        return total_day
                