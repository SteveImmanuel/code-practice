class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        switch_one = []
        switch_zero = []
        
        total_one = 0
        for i in range(len(s)):
            switch_one.append(total_one)
            if s[i] == '1':
                total_one += 1
                
        total_zero = 0
        for i in range(len(s) - 1, -1, -1):
            switch_zero.append(total_zero)
            if s[i] == '0':
                total_zero += 1
                
        min_switch = len(s)
        for i in range(len(s)):
            min_switch = min(min_switch, switch_one[i] + switch_zero[len(s) - 1 - i])
        # print(switch_zero[::-1])
        # print(switch_one)
        return min_switch