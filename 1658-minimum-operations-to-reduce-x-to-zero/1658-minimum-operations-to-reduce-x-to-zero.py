class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        pre_sum = [0] * len(nums)
        post_sum = [0] * len(nums)
        
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            pre_sum[i] = cur

        cur = 0
        for i in range(len(nums) - 1, -1, -1):
            cur += nums[i]
            post_sum[i] = cur     
        
        pre_dict = {val:i+1 for i,val in enumerate(pre_sum)}
        post_dict = {val:len(post_sum)-i for i,val in enumerate(post_sum)}
        
        min_op = float('inf')
        for key in pre_dict:
            total = pre_dict[key]
            rem = x - key
            if rem == 0:
                min_op = min(min_op, total)
            elif rem in post_dict and pre_dict[key] + post_dict[rem] <= len(nums):
                total += post_dict[rem]
                min_op = min(min_op, total)
                
        for key in post_dict:
            total = post_dict[key]
            rem = x - key
            if rem == 0:
                min_op = min(min_op, total)
            elif rem in pre_dict and pre_dict[rem] + post_dict[key] <= len(nums):
                total += pre_dict[rem]
                min_op = min(min_op, total)
                

        if min_op > len(nums):
            return -1
        return min_op