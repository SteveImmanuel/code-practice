class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        l, h = min(nums), max(nums)
        while l < h:
            m = (l + h) // 2
            if not self.is_valid(nums, m):
                l = m + 1
            else:
                h = m
        return l
        
    def is_valid(self, nums, min_max):
        remainder = 0
        for i in range(len(nums) - 1, -1, -1):
            cur_num = remainder + nums[i]
            if cur_num > min_max:
                remainder = cur_num - min_max
            else:
                remainder = 0
        # print(remainder)
        return remainder == 0