class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        front = Counter()
        end = Counter(s[1:])
        total = set()
        
        for pivot in range(1, len(s) - 1):
            front[s[pivot-1]] += 1
            end[s[pivot]] -= 1
            if end[s[pivot]] <= 0:
                del end[s[pivot]]
            for key in front:
                if key in end:
                    total.add(key + s[pivot] + key)
            # print(front, end, pivot, total)            
        return len(total)
