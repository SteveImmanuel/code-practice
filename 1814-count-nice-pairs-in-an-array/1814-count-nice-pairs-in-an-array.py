class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rev_nums = [self.rev(num) for num in nums]
        pair_dict = defaultdict(int)
        for i in range(len(nums)):
            pair_dict[nums[i] - rev_nums[i]] += 1
        
        res = 0
        MOD = 1000000007
        for val in pair_dict.values():
            res += ((val * (val - 1)) // 2) % MOD
        res %= MOD
        return res
    
    def rev(self, num):
        res = 0
        while num > 0:
            num, mod = divmod(num, 10)
            res = res * 10 + mod
        return res