class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        multiplier = 1
        base = 26
        while multiplier * base < columnNumber:
            multiplier *= base
        
        base_num = []
        while multiplier > 0:
            div, columnNumber = divmod(columnNumber, multiplier)
            base_num.append(div)
            multiplier //= base

        has_debt = False
        for i in range(len(base_num) - 1, -1, -1):
            if base_num[i] == 0:
                if i == 0:
                    break
                    
                base_num[i] = 26
                if base_num[i-1] > 0:
                    base_num[i-1] -= 1
                    has_debt = False
                else:
                    base_num[i-1] = 25
                    has_debt = True
            elif has_debt:
                if base_num[i-1] > 0:
                    base_num[i-1] -= 1
                    has_debt = False
                else:
                    base_num[i-1] = 25
                    has_debt = True
        
        string_lowercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        string_map = {i+1:string_lowercase[i] for i in range(26)}
        string_map[0] = ''
        res = ''.join(map(lambda x: string_map[x], base_num))
        return res