# https://leetcode.com/problems/longest-common-prefix/
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur_idx = 0
        len_strs = map(len, strs)
        min_len = min(len_strs)

        while cur_idx < min_len:
            anchor_letter = strs[0][cur_idx]
            found = False
            
            for str in strs:
                if str[cur_idx] != anchor_letter:
                    found = True
                    break
            
            if found:
                break
            else:
                cur_idx += 1
        
        return strs[0][:cur_idx]


sol = Solution()
strs = ["dog","racecar","car"]
strs = [""]
print(sol.longestCommonPrefix(strs))