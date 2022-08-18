# https://leetcode.com/problems/reduce-array-size-to-the-half/
from typing import List
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        min_remove = len(arr) // 2
        occ_count = [(key,val) for key, val in Counter(arr).items()]
        occ_count = sorted(occ_count, key=lambda x:x[1], reverse=True)
        
        total_remove = 0
        i = 0
        while i < len(occ_count):
            total_remove += occ_count[i][1]
            i += 1
            if total_remove >= min_remove:
                break
        return i

sol = Solution()
arr = [7,2]
print(sol.minSetSize(arr))        