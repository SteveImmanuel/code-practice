class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 1000000007
        
        final_nums = [num + d if s[i] == 'R' else num - d for i, num in enumerate(nums)]
        final_nums.sort()
        # print(final_nums)
        last_sum = 0
        for i in range(1, len(final_nums)):
            last_sum += abs(final_nums[i] - final_nums[0]) % MOD
        
        total = last_sum
        multiplier = len(final_nums) - 1
        while multiplier > 1:
            idx = len(final_nums) - multiplier
            minus_len = abs(final_nums[idx] - final_nums[idx - 1]) % MOD
            cur_sum = (last_sum - multiplier * minus_len) % MOD
            total += cur_sum % MOD
            last_sum = cur_sum
            multiplier -= 1
        
        return total % MOD
            