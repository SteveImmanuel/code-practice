class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        total_zeros = s.count('0')
        cur_zeros = 0
        length = len(s)
        for i in range(len(s) - 1):
            if s[i] == '0':
                cur_zeros += 1
            cur_ones = length - (i + 1) - (total_zeros - cur_zeros)
            max_score = max(max_score, cur_zeros + cur_ones)
            # print(i, cur_zeros, cur_ones, max_score)
        return max_score
            
            
        
