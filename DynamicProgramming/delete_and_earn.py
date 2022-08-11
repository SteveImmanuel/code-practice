# https://leetcode.com/problems/delete-and-earn/
from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        occ = Counter(nums)
        sorted_nums = sorted(set(nums))
        mem = [None] * len(sorted_nums)
        max_poin = 0

        for i in range(len(mem)):
            num = sorted_nums[i]
            if i==0:
                mem[i] = (num * occ[num], 0)
            else:

                # print(num, occ, num-1 in occ)
                if num-1 in occ:
                    mem[i] = (num * occ[num] + mem[i-1][1], max(mem[i-1]))
                else:
                    mem[i] = (num * occ[num] + max(mem[i-1]), max(mem[i-1]))
            
            max_poin = max(max_poin, max(mem[i]))
        
        return max_poin



sol = Solution()
nums = [2,2,3,3,3,4]
print(sol.deleteAndEarn(nums))