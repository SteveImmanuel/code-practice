class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        pos_num = x
        if x < 0:
            pos_num = -x
            neg = True
        max_num = 2**31
        res = 0
        while pos_num > 0:
            pos_num, mod_res = divmod(pos_num, 10)
            res = res*10 + mod_res
            if res >= max_num:
                return 0
        res = res * (-1 if neg else 1)
        return res