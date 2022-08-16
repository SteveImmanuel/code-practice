# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_occ = Counter(s)
        for i in range(len(s)):
            if count_occ[s[i]] == 1:
                return i
        return -1

sol = Solution()
s = "leetcode"
print(sol.firstUniqChar(s))