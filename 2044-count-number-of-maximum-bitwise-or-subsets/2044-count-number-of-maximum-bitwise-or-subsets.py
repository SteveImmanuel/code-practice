class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_possible = ['0'] * 17
        for i in range(16, -1, -1):
            shift = 16 - i
            # print(shift)
            for num in nums:
                # print(num, shift, num >> shift)
                if (num >> shift) & 1 == 1:
                    max_possible[i] = '1'
                    break
        # print(max_possible)
        max_possible = '0b' + ''.join(max_possible)
        max_possible = int(max_possible, 2)
        # print(max_possible)
        
        total = 0
        for i in range(1, 2 ** len(nums)):
            mask = str(bin(i))[2:]
            mask = (len(nums) - len(mask)) * '0' + mask
            cnum = 0
            for j in range(len(mask)):
                if mask[j] == '1':
                    cnum = cnum | nums[j]
            # print(cnum, mask)
            if cnum == max_possible:
                total += 1
        
        
        return total