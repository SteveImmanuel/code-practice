class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        current_int = 1
        op = []
        for num in target:
            if num == current_int:
                op.append('Push')
                
            else: # guaranteed current_int < num
                for i in range(num - current_int):
                    op.append('Push')
                    op.append('Pop')
                op.append('Push')
                
            current_int = num + 1
        return op
                