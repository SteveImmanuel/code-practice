# https://leetcode.com/problems/restore-ip-addresses/

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restoreRec(s, 3)

    def is_num_valid(self, s):
        num = int(s)
        return len(s) == len(str(num)) and num >=0 and num <= 255

    def restoreRec(self, s, num_dots):
        if num_dots == 0:
            if len(s) > 0 and self.is_num_valid(s):
                return [s]
            return []

        result = []
        for i in range(1, 4):
            if len(s) >= i:
                candidate = s[:i]
                if self.is_num_valid(candidate):
                    all_rest = self.restoreRec(s[i:], num_dots-1)
                    for rest in all_rest:
                        result.append(f'{candidate}.{rest}')
        
        return result

sol = Solution()
s = '101023'
print(sol.restoreIpAddresses(s))
