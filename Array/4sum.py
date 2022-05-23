# https://leetcode.com/problems/4sum/
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        len_nums = len(nums)
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        result = set()

        for i in range(len_nums):
            for j in range(i+1, len_nums):
                for k in range(j+1, len_nums):
                    last_num = target - (nums[i] + nums[j] + nums[k])
                    nums_dict[nums[i]] -= 1
                    nums_dict[nums[j]] -= 1
                    nums_dict[nums[k]] -= 1

                    if last_num in nums_dict and nums_dict[last_num] >= 1:
                        possible = [nums[i], nums[j], nums[k], last_num]
                        possible.sort()
                        result.add(tuple(possible))
                    nums_dict[nums[i]] += 1
                    nums_dict[nums[j]] += 1
                    nums_dict[nums[k]] += 1

        
        return list(result)

sol = Solution()        
# nums = [1,0,-1,0,-2,2]
# target = 0
nums = [2,2,2,2,2]
target = 8
print(sol.fourSum(nums, target))
