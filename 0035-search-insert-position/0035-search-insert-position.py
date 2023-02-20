class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)

        while l < h:
            m = (l+h) // 2
            if nums[m] < target:
                l = m + 1
            else:
                h = m
        return l