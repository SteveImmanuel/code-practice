# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_dict = {}
        val_set = set()
        for i in range(len(s)):
            if s[i] not in map_dict and t[i] not in val_set:
                map_dict[s[i]] = t[i]
                val_set.add(t[i])
            elif s[i] not in map_dict and t[i] in val_set:
                return False
            else:
                if map_dict[s[i]] != t[i]:
                    return False
        return True

sol = Solution()
s = "paper"
t = "title"
# s = "badc"
# t = "baba"
print(sol.isIsomorphic(s, t))