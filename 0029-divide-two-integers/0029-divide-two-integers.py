class Solution:
    def mydivmod(self, a, b):
        res = 0
        while a > 0:
            res += 1
            a -= b
        if a == 0:
            return res, 0
        return res - 1, a + b
    
    def divide(self, dividend: int, divisor: int) -> int:
        flip_neg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        multiplier = 1
        cur_divisor = divisor
        while cur_divisor < dividend:
            multiplier <<= 1
            cur_divisor <<= 1
        if cur_divisor > dividend:
            multiplier >>= 1
            cur_divisor >>= 1
        # print(cur_divisor, multiplier)
        
        res = 0
        remaining = dividend
        while remaining > 0 and multiplier > 0:
            div, remaining = self.mydivmod(remaining, cur_divisor)
            res += div * multiplier
            cur_divisor >>= 1
            multiplier >>= 1
        # print(res, remaining, cur_divisor)
            
        if flip_neg:
            res *= -1
        res = max(min(res, 2**31 - 1), -(2**31))
        return res
        
        
    
    # # bruteforce TLE
    # def divide(self, dividend: int, divisor: int) -> int:
    #     res = 0
    #     flip_neg = (dividend < 0) ^ (divisor < 0)
    #     dividend = abs(dividend)
    #     divisor = abs(divisor)
    #     cur = 0
    #     while cur < dividend:
    #         res += 1
    #         cur += divisor
    #     if cur > dividend:
    #         res -= 1
    #     print(res, flip_neg)
    #     if flip_neg:
    #         res *= -1
    #     return res