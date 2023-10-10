class Solution:
    def minOperations(self, nums: List[int]) -> int:
        len_ori = len(nums)
        nums = list(set(nums))
        total_duplicate = len_ori - len(nums)
        nums.sort()
        
        start_num = None
        for i, num in enumerate(nums):
            last = num + len_ori - 1
            last_idx = bisect_right(nums, last)
            total_cover = last_idx - i
            if start_num is None or total_cover > start_num[1]:
                start_num = (num, total_cover)
            
        start_num = start_num[0]
        expected_arr = set([x for x in range(start_num, start_num + len_ori)])
        total_op = 0
        for num in nums:
            if num not in expected_arr:
                total_op += 1
        return total_op + total_duplicate
