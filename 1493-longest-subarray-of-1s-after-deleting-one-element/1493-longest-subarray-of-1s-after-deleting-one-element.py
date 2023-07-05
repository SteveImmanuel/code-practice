class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        count_arr = []
        
        one_found = False
        cur_count = 0
        last_digit = None

        while i < len(nums):
            if nums[i] == 0:
                if one_found:
                    if last_digit is None or last_digit == nums[i]:
                        cur_count += 1
                    else:
                        count_arr.append(cur_count)
                        cur_count = 1    
            else:
                if last_digit is None or last_digit == nums[i]:
                    cur_count += 1
                else:
                    if one_found:
                        count_arr.append(cur_count)
                    cur_count = 1
                
                if not one_found:
                    one_found = True
                
            last_digit = nums[i]
            i += 1
        if one_found:
            count_arr.append(cur_count)
        # print(count_arr)
        max_len = 0
        for i in range(1, len(count_arr), 2):
            if i + 1 < len(count_arr):            
                if count_arr[i] == 1:
                    max_len = max(max_len, count_arr[i-1] + count_arr[i+1])
                else:
                    max_len = max(max_len, count_arr[i-1], count_arr[i+1])
            else:
                max_len = max(max_len, count_arr[i-1])
                
                
        if len(count_arr) == 1:
            if count_arr[0] == len(nums):
                max_len = count_arr[0] - 1
            else:
                max_len = count_arr[0]
        
        return max_len