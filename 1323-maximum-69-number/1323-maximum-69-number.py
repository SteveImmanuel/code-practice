class Solution:
    def maximum69Number (self, num: int) -> int:
        reverse_num = 0
        while num > 0:
            num, unit = divmod(num, 10)
            reverse_num = 10*reverse_num + unit
        
        res = 0
        flip = False
        while reverse_num > 0:
            reverse_num, unit = divmod(reverse_num, 10)
            if unit == 6 and not flip:
                unit = 9
                flip = True
            res = 10*res + unit
        return res