class Solution:
    def smallestNumber(self, num: int) -> int:
        mul = 1
        if num < 0:
            mul = -1
        digits = [0 for _ in range(10)]
        for digit in str(num * mul):
            digits[int(digit)] += 1
        
        if num >= 0:
            res = []
            for i in range(10):
                idx = i
                if digits[idx] > 0:
                    res.append(str(idx) * digits[idx])
            if digits[0] > 0 and len(res) > 1:
                res[0] = res[1][0] + res[0]
                if len(res[1]) > 1:
                    res[1] = res[1][0] * (len(res[1]) - 1)
                else:
                    res.pop(1)
            
        else:
            res = []
            for i in range(9, -1, -1):
                idx = i
                if digits[idx] > 0:
                    res.append(str(idx) * digits[idx])
            print(res)
        
        res = ''.join(res)
        return int(res) * mul