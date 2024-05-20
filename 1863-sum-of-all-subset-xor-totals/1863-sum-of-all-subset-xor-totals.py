class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        total = 0
        for i in range(1, 2 ** (len(nums))):
            cur_xor = 0
            mask = i
            idx = len(nums) - 1
            while mask > 0:
                if mask & 1 == 1:
                    cur_xor = cur_xor ^ nums[idx]
                idx -= 1
                mask = mask >> 1
            total += cur_xor
        
        return total
                