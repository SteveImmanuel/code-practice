# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
from typing import List
from collections import defaultdict

class Solution:
    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        diff_dict = defaultdict(lambda: [])
        for i in range(10):
            if i + k <= 9:
                diff_dict[str(i)].append(str(i+k))
            if i - k >= 0 and k != 0:
                diff_dict[str(i)].append(str(i-k))
        print(diff_dict)
        res = []
        for start_digit in diff_dict.keys():
            if start_digit == '0':
                continue
            res += self.build_digit(start_digit, n, diff_dict)
        return res

    def build_digit(self, current_digit, remaining_digit, diff_dict):
        if remaining_digit == 1:
            return [current_digit]
        else:
            result = []
            for possible_digit in diff_dict[current_digit]:
                for remaining in self.build_digit(possible_digit, remaining_digit-1, diff_dict):
                    result.append(current_digit + remaining)
            return result

sol = Solution()
# print(sol.permute('0123'))
print(sol.numsSameConsecDiff(2, 0))        