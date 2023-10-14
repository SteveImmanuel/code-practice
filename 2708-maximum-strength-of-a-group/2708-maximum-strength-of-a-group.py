class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        zero = [num for num in nums if num == 0]        
        if len(pos) == 0 and len(neg) == 1:
            if len(zero) == 0:
                return neg[0]
            else:
                return 0
        elif len(pos) == 0 and len(neg) == 0:
            return 0
        
        
        strength = 1
        for num in pos:
            strength *= num
        
        neg.sort()
        max_idx = len(neg) if len(neg) % 2 == 0 else len(neg) - 1

        for i in range(max_idx):
            strength *= neg[i]
        return strength