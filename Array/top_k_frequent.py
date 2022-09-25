# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(lambda: 0)
        for num in nums:
            num_dict[num] += 1
        
        arr = list(num_dict.items())
        arr.sort(key=lambda x:x[1], reverse=True)
        print(arr)
        return list(map(lambda x:x[0], arr[:k]))


sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.topKFrequent(nums, k))