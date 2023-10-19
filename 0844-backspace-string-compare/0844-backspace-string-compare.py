class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.type(s) == self.type(t)
    
    def type(self, s):
        res = []
        for char in s:
            if char == '#':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(char)
        return res