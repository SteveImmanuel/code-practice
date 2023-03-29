class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        cum_sum_reversed = []
        cur_sum = 0
        for num in satisfaction:
            cur_sum += num
            cum_sum_reversed.append(cur_sum)

        # print(satisfaction)
        # print(cum_sum_reversed)
        
        max_satisfaction = 0
        cur_satisfaction = sum(cum_sum_reversed)
        for i in range(len(satisfaction)):
            if i > 0:
                cur_satisfaction -= cum_sum_reversed[len(cum_sum_reversed) - i]
            max_satisfaction = max(max_satisfaction, cur_satisfaction)
        return max_satisfaction
            