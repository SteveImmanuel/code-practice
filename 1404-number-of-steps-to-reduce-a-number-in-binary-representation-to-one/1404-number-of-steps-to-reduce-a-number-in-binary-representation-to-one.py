class Solution:
    def numSteps(self, s: str) -> int:
        total = 0
        carry = 0
        for i in range(len(s) - 1, -1, -1):
            cur_num = int(s[i])
            if carry > 0:
                cur_num += carry
                if cur_num == 2:
                    cur_num = 0
                    carry = 1
                else:
                    carry = 0
            
            if cur_num == 0:
                total += 1
            else:
                if i > 0:
                    carry = 1
                    total += 2
            # print(total, cur_num , carry)
        return total