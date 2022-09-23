# https://leetcode.com/problems/product-of-array-except-self/
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        mul = 1
        for i in range(1, len(nums)):
            mul *= nums[i-1]
            res[i] = mul
        
        mul = 1
        for i in range(len(nums)-2, -1, -1):
            mul *= nums[i+1]
            res[i] *= mul
            
        return res
sol = Solution()
nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums))