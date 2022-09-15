# https://leetcode.com/problems/find-original-array-from-doubled-array/
from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        sorted_arr = sorted(changed)
        num_dict = Counter(sorted_arr)

        res = []
        for num in sorted_arr:
            if num in num_dict and 2*num in num_dict:
                res.append(num)
                num_dict[num] -= 1
                num_dict[2*num] -= 1
                if num_dict[num] == 0:
                    del num_dict[num]
                if num_dict[num*2] == 0:
                    del num_dict[num*2]
        if len(num_dict) == 0:
            return res
        return []


sol = Solution()
changed = [1,3,4,2,6,8]
changed = [6,3,0,1]
changed = [1]
print(sol.findOriginalArray(changed))
        