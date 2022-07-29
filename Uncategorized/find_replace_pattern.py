# https://leetcode.com/problems/find-and-replace-pattern/
from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if self.is_valid(word, pattern):
                res.append(word)
        return res

    def is_valid(self, word, pattern):
        i = 0
        map_dict = {}
        values_set = set()

        for i, char in enumerate(word):
            if char in map_dict:
                if map_dict[char] != pattern[i]:
                    return False
            else:
                if pattern[i] not in values_set:
                    map_dict[char] = pattern[i]
                    values_set.add(pattern[i])
                else:
                    return False
        return True


sol = Solution()
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
words = ["a","b","c"]
pattern = "a"
print(sol.findAndReplacePattern(words, pattern))