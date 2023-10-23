class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        if n == 1:
            return True
        
        div, mod = divmod(n, 4)
        if mod != 0:
            return False
        
        return self.isPowerOfFour(div)