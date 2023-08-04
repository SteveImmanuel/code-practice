class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # mem = {}
        # self.wordbreak_rec(s, wordDict, mem)
        # print(mem)
        # return mem[s]
        return self.wordbreak_rec(s, wordDict, {})
        
    def wordbreak_rec(self, s, word_dict, mem):
        if s not in mem:
            if s in word_dict:
                mem[s] = True
            else:
                can_break = False
                for i in range(1, len(s)):
                    f_part = s[:i]
                    b_part = s[i:]
                    if f_part in word_dict and self.wordbreak_rec(b_part, word_dict, mem):
                        can_break = True
                        break
                mem[s] = can_break
            
        return mem[s]