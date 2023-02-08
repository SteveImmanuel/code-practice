class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        multiply_dict = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                multiply_dict[nums[i]*nums[j]] += 1

        total_nums = 0
        for value in multiply_dict.values():
            if value < 2:
                continue
            total_nums += value * (value-1) * 4


        return total_nums