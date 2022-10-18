class Solution:
    def add(self, num1: str, num2: str) -> str:
        if len(num1) == 1 and len(num2) == 1:
            res = int(num1) + int(num2)
            return str(res)
        
        max_len = max(len(num1), len(num2))
        if len(num1) > len(num2):
            num2 = '0'*(len(num1) - len(num2)) + num2
        else:
            num1 = '0'*(len(num2) - len(num1)) + num1

        res = ''
        excess = '0'
        for i in range(max_len-1, -1, -1):
            add_res = self.add(num1[i], num2[i])
            add_res = self.add(add_res, excess)

            if i != 0:
                if len(add_res) != 1:
                    excess = add_res[0]
                else:
                    excess = '0'
                res = add_res[-1] + res
            else:
                res = add_res + res
        return res

    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 1 and len(num2) == 1:
            res = int(num1) * int(num2)
            return str(res)
        
        if len(num1) > len(num2):
            multipliee = num1
            multiplier = num2
        else:
            multipliee = num1
            multiplier = num2

        global_res = '0'
        for i in range(len(multiplier)-1, -1, -1):
            res = ''
            excess = '0'
            for j in range(len(multipliee)-1, -1, -1):
                mul_res = self.multiply(multipliee[j], multiplier[i])
                mul_res = self.add(mul_res, excess)

                if j != 0:
                    if len(mul_res) != 1:
                        excess = mul_res[0]
                    else:
                        excess = '0'
                    res = mul_res[-1] + res
                else:
                    res = mul_res + res
            res += '0' * (len(multiplier)-1 - i)
            global_res = self.add(res, global_res)
        
        i = 0
        while global_res[i] == '0' and i < len(global_res) - 1:
            i += 1
        return global_res[i:]