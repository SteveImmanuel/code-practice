class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total = 0
        blacklist = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    blacklist.append(2 ** (len(nums) - 1 - i) + 2 ** (len(nums) - 1 - j))
        
        for mask in range(1, 2 ** (len(nums))):
            valid = True
            for item in blacklist:
                if mask & item == item:
                    valid = False
                    break
            if valid:
                total += 1
        return total
        # for mask in range(1, 2**(len(nums))):
        #     rightmost_idx = len(nums) - 1
        #     print(bin(mask), rightmost_idx, mask & 1)
        #     while mask & 1 != 1:
        #         mask = mask >> 1
        #         rightmost_idx -= 1
        #     # print(mask, rightmost_idx)
        #     leftmost_idx = rightmost_idx
        #     while mask > 0:
        #         mask = mask >> 1
        #         leftmost_idx -= 1
        #     leftmost_idx += 1
        #     if leftmost_idx == rightmost_idx:
        #         total += 1
        #     elif nums[rightmost_idx] - nums[leftmost_idx]