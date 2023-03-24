class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_occ = defaultdict(int)
        
        cum_sum = 0
        total = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            
            if cum_sum == k:
                total += 1

            remainder = cum_sum - k
            total += sum_occ[remainder]
            
            sum_occ[cum_sum] += 1
        
        return total
    
#     this one only works if the numbers are all > 0
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         l = 0
#         r = 0
#         total = 0
#         current_sum = nums[0]
        
#         while l < len(nums) and r < len(nums):
#             print(current_sum, l ,r )
#             if current_sum >= k:
#                 if current_sum == k:
#                     total += 1
#                 current_sum -= nums[l]
#                 l += 1
#             elif current_sum < k:
#                 r += 1
#                 if r < len(nums):
#                     current_sum += nums[r]
        
#         return total