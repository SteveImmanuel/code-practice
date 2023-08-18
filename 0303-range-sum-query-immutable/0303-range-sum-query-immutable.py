class NumArray:

    def __init__(self, nums: List[int]):
        # self.cur_sum = sum(nums)
        # self.l = 0
        # self.r = len(nums) - 1
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right+1):
            total += self.nums[i]
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)