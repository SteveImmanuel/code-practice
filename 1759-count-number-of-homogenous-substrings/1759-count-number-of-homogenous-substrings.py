class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 1000000007
        total = 0
        cur_len = 1
        cur_word = s[0]
        for i in range(1, len(s)):
            if s[i] == cur_word:
                cur_len += 1
            else:
                total += self.count(cur_len) % MOD
                cur_len = 1
                cur_word = s[i]
        
        total += self.count(cur_len) % MOD
        return total % MOD
                
    
    def count(self, n):
        return ((n + 1) * n) // 2