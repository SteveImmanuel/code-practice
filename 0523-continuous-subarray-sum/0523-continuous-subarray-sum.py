class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         cum_sum_arr = [0]
#         cur_sum = 0
#         for num in nums:
#             cur_sum += num % k
#             cum_sum_arr.append(cur_sum)
            
#         # print(cum_sum_arr)
#         for i in range(1, len(cum_sum_arr)):
#             for j in range(i-1):
#                 if (cum_sum_arr[i] - cum_sum_arr[j]) % k == 0:
#                     return True
        
#         return False
    
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cum_sum_set = set([0])
        cur_sum = 0
        
        for i in range(len(nums)):
            cur_sum = (cur_sum + nums[i]) % k
            
            if i >= 1:
                if cur_sum in cum_sum_set:
                    return True
                
                cum_sum_set.add((cur_sum-nums[i]) % k)
            
        
        return False