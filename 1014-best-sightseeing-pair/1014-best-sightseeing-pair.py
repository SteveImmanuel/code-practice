class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        prev_best_idx = 0
        
        for i in range(1, len(values)):
            ans = max(ans, values[prev_best_idx] + values[i] + prev_best_idx - i)
            if values[prev_best_idx] + prev_best_idx < values[i] + i:
                prev_best_idx = i
        
        return ans