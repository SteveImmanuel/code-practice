class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        found = False
        i = 1
        while i <= len(s) and not found:
            pat = s[:i]
            if self.check_rec(s[i:], pat):
                found = True
            i += 1
        return found
    
    def check_rec(self, s, pat):
        n = len(pat)
        if len(s) < n:
            return False
        
        head = s[:n]
        tail = s[n:]
        
        if head == pat:
            if len(tail) == 0:
                return True
            return self.check_rec(tail, pat)
    
        return False