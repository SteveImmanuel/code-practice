# https://leetcode.com/problems/maximum-product-subarray/
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        idx_zero = None
        i = 0
        while i < len(nums) and idx_zero is None:
            if nums[i] == 0:
                idx_zero = i
            i += 1

        if idx_zero is not None:
            return max(0, self.maxProduct(nums[:idx_zero]), self.maxProduct(nums[idx_zero+1:]))
        else:
            return self.maxProductSub(nums)

    def maxProductSub(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        global_max = 1
        for num in nums:
            global_max *= num
        
        if global_max < 0:
            valid_left = False
            product_left = 1
            i = 0
            while nums[i] > 0:
                product_left *= nums[i]
                i += 1
            product_left *= nums[i]
            valid_left = i != len(nums) - 1

            valid_right = False
            product_right = 1
            i = len(nums) - 1
            while nums[i] > 0:
                product_right *= nums[i]
                i -= 1
            product_right *= nums[i]
            valid_right = i != 0

            temp_global_max = global_max
            if valid_left:
                global_max = max(global_max, temp_global_max // product_left)
            if valid_right:
                global_max = max(global_max, temp_global_max // product_right)

        return global_max


sol = Solution()
nums = [3,-1,4]
print(sol.maxProduct(nums))