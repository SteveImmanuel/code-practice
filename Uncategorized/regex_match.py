# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatchRec(self, s: str, p: str, mem) -> bool:
        key = f'{s}#{p}'
        if key in mem:
            return mem[key]
        if p == '':
            mem[key] = s == ''
            return s == ''

        # abcd a*bcd
        if len(s) > 0 and s[0] == p[0]:
            matched_char = s[0]
            s_rest = s[1:]
            p_rest = p[1:]

            if len(p_rest) > 0 and p_rest[0] == '*':
                if len(p_rest) > 1 and p_rest[1]:
                    p_rest = p_rest[1:] # cd

                    candidate = []
                    i = 0

                    while i < len(s) and s[i] == matched_char:
                        candidate.append(i)
                        i += 1
                    candidate.append(i)

                    is_matched = [self.isMatchRec(s[idx:], p_rest, mem) for idx in candidate]
                    res = False
                    for match in is_matched:
                        res = res or match

                    mem[key] = res
                    return res

                else:
                    while len(s_rest) > 0 and s_rest[0] == matched_char:
                        s_rest = s_rest[1:]
                    
                    res = self.isMatchRec(s_rest, p_rest[1:], mem)
                    mem[key] = res
                    return res
            else:
                res = self.isMatchRec(s_rest, p_rest, mem)
                mem[key] = res
                return res

        # abcd .*cd
        elif len(s) > 0 and p[0] == '.':
            p_rest = p[1:]

            if len(p_rest) == 1 and p_rest[0] == '*':
                mem[key] = True
                return True
            if len(p_rest) > 1 and p_rest[0] == '*': # *cd
                p_rest = p_rest[1:] # cd
                candidate = [i for i in range(len(s) + 1)]

                is_matched = [self.isMatchRec(s[idx:], p_rest, mem) for idx in candidate]
                res = False
                for match in is_matched:
                    res = res or match

                mem[key] = res
                return res
            else:
                res = self.isMatchRec(s[1:], p_rest, mem)
                mem[key] = res
                return res
        
        # abcdqwe b*abcdqwe
        else:
            if len(p) > 1 and p[1] == '*':
                res = self.isMatchRec(s, p[2:], mem)
                mem[key] = res
                return res
            else:
                mem[key] = False
                return False
    
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}
        return self.isMatchRec(s, p, mem)

sol = Solution()
s="abcaaaaaaabaabcabac"
p=".*ab.a.*a*a*.*b*b*"
print(sol.isMatch(s, p))