class Solution:
#     def bisect_right(self, arr, low, high, val):
#         l = low
#         h = high
        
#         while l < h:
#             m = (l + h) // 2
#             if arr[m][0] <= val:
#                 l = m + 1
#             else:
#                 h = l
#         return l
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = []
        # loc_dict = defaultdict(list) # needed if the nums[i] can be negative to handle multiple same values
        # since the nums[i] >= 1, the prefix sum is guaranteed unique
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix_sum.append(total)

        min_length = None
        for i in range(len(nums)):
            if prefix_sum[i] < target:
                continue
            
            budget = prefix_sum[i] - target
            cur_min = i + 1

            if budget > 0:
                idx = bisect_right(prefix_sum, budget, 0, i + 1)
                if idx >= 0:
                    cur_min -= idx
            if min_length is None or cur_min < min_length:
                min_length = cur_min
        
        if min_length is None:
            return 0
        return min_length
