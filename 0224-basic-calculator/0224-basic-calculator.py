class Solution:
    def atomic(self, x1, op, x2):
        if op == '+':
            return x1 + x2
        else:
            return x1 - x2
        
    def calculate(self, s: str) -> int:
        res = self._calc(s, 0)
        # print(res)
        return res[1]

    def _calc(self, s, idx):
        # print('evaluating', s[idx:])
        f_num = 0
        s_num = None
        op = None
        while idx < len(s):
            # print('idx:', idx, 'char:', s[idx])
            # print('before', f_num, s_num, op)

            if s[idx] in ['+', '-']:
                if s_num is not None:
                    if op is not None:
                        f_num = self.atomic(f_num, op, s_num)
                        op = None
                    else:
                        f_num = s_num
                    s_num = None
                op = s[idx]
                idx += 1
            elif s[idx].isnumeric():
                if s_num is None:
                    s_num = int(s[idx])
                else:
                    s_num = s_num * 10 + int(s[idx])
                idx += 1
            elif s[idx] == '(':
                assert s_num is None
                idx, s_num = self._calc(s, idx + 1)
                if op is not None:
                    f_num = self.atomic(f_num, op, s_num)
                    op = None
                else:
                    f_num = s_num
                s_num = None
            elif s[idx] == ')':
                idx += 1
                break
            else:
                idx += 1
            
            # print('after', f_num, s_num, op)
            # print()

        # print('before', f_num, s_num, op)
        if s_num is not None:
            if op is not None:
                f_num = self.atomic(f_num, op, s_num)
                op = None
            else:
                f_num = s_num
            s_num = None
        # print('after', f_num, s_num, op)
        
        return idx, f_num