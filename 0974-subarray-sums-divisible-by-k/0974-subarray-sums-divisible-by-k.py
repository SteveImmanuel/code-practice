class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         total = 0
#         last_dict = Counter()
        
#         for num in nums:
#             current_dict = Counter()
#             if num % k == 0:
#                 current_dict[0] = last_dict[0]
#             for key, val in last_dict.items():
#                 if key == 0:
#                     continue
#                 else:
#                     current_dict[(key + num) % k] += val
                    
#             current_dict[num % k] += 1 + (last_dict[0] if num % k != 0 else 0)
#             total += current_dict[0]
#             # print(num, last_dict, current_dict, total)
#             last_dict = current_dict
        
#         return total

        prefix_sum = [None] * len(nums)
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            prefix_sum[i] = cur_sum % k
            
        total = 0
        occ_remainder = Counter(prefix_sum)
        for key, value in occ_remainder.items():
            if value > 1:
                total += ((value - 1) * value) // 2
            if key == 0:
                total += value
        return total
            