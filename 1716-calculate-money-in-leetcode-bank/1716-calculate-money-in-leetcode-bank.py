class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.calc(n, 0)
        
    def calc(self, n, multiplier):
        if n < 7:
            return multiplier * n + (((1 + n) * n) // 2)
        else:
            return 7 * multiplier + 28 + self.calc(n - 7, multiplier + 1)