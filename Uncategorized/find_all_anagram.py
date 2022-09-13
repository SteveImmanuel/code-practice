# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        occ_count = Counter(p)
        if len(p) > len(s):
            return result

        for i in range(len(s)):
            if i < len(p):
                occ_count[s[i]] -= 1
                if occ_count[s[i]] == 0:
                    del occ_count[s[i]]

                if i == len(p) - 1:
                    if len(occ_count) == 0:
                        print(i, len(p), i - len(p) + 1)
                        result.append(i - len(p) + 1)
            else:
                occ_count[s[i]] -= 1
                if occ_count[s[i]] == 0:
                    del occ_count[s[i]]

                occ_count[s[i - len(p)]] += 1
                if occ_count[s[i - len(p)]] == 0:
                    del occ_count[s[i - len(p)]]
                
                if len(occ_count) == 0:
                    result.append(i - len(p) + 1)
            print(occ_count, s[i])
        return result


        



sol = Solution()
s = "cbaebabacd"
p = "abc"
# s = "abab"
# p = "ab"
print(sol.findAnagrams(s,p))