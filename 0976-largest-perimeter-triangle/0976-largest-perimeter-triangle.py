class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        num_sort = sorted(nums)
        for i in range(len(nums)-3, -1, -1):
            if num_sort[i] + num_sort[i+1] > num_sort[i+2]:
                return num_sort[i] + num_sort[i+1] + num_sort[i+2]
        return 0