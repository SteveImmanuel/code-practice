# https://leetcode.com/problems/decode-string/?envType=study-plan&id=level-1

class Solution:
    def decode_bracket(self, s, start_idx):
        total_bracket = 1
        number_buffer = ''
        i = start_idx
        res = ''

        while i < len(s) and total_bracket > 0:
            if 97 <= ord(s[i]) <= 122:
                res += s[i]
            elif s[i] == '[':
                i, text = self.decode_bracket(s, i+1)
                res += int(number_buffer) * text
                number_buffer = ''
                i -= 1
            elif s[i] == ']':
                total_bracket -= 1
            else:
                number_buffer += s[i] 
            i += 1
        
        return i, res

    def decodeString(self, s: str) -> str:
        return self.decode_bracket(s, 0)[1]
        # number_buffer = ''
        # text_buffer = ''
        # on_bracket = False
        # res = ''

        # i = 0
        # while i < len(s):
        #     if 97 <= ord(s[i]) <= 122:
        #         if on_bracket:
        #             text_buffer += s[i]
        #         else:
        #             res += s[i]
        #     elif s[i] == '[':
        #         on_bracket = True
        #     elif s[i] == ']':
        #         on_bracket = False
        #     else:
        #         number_buffer += s[i]

sol = Solution()
s = "3[a2[c]]"
s = '2[ab4[c]]3[2[c]4[d]]ef'
print(sol.decodeString(s))