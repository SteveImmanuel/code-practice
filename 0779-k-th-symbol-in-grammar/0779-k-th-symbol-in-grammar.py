class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1 and k == 1:
            return 0
        else:
            parent_k = ((k - 1) // 2) + 1
            parent = self.kthGrammar(n - 1, parent_k)
            
            if k % 2 == 0:
                return 1 - parent
            else:
                return parent