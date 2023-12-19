class Solution:
    def atomic(self, x1, op, x2):
        if op == '+':
            return x1 + x2
        else:
            return x1 - x2
        
    def calculate(self, s: str) -> int:
        res = self._calc(s, 0)
        return res[1]

    def _eval(self, f_num, op, s_num):
        if s_num is not None:
            if op is not None:
                f_num = self.atomic(f_num, op, s_num)
                op = None
            else:
                f_num = s_num
            s_num = None
        return f_num, op, s_num

    def _calc(self, s, idx):
        f_num = 0
        s_num = None
        op = None
        while idx < len(s):
            if s[idx] in ['+', '-']:
                f_num, op, s_num = self._eval(f_num, op, s_num)
                op = s[idx]
            elif s[idx].isnumeric():
                if s_num is None:
                    s_num = int(s[idx])
                else:
                    s_num = s_num * 10 + int(s[idx])
            elif s[idx] == '(':
                idx, s_num = self._calc(s, idx + 1)
                f_num, op, s_num = self._eval(f_num, op, s_num)
                idx -= 1
            elif s[idx] == ')':
                idx += 1
                break
            
            idx += 1
        
        f_num, op, s_num = self._eval(f_num, op, s_num)
        
        return idx, f_num