# https://leetcode.com/problems/word-break/
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memory = {}
        res = self.wordBreakRec(s, word_set, memory)
        print(memory)
        return res

    def wordBreakRec(self, s, word_set, memory):
        for space_pos in range(1, len(s)+1):
            first_part = s[:space_pos]
            second_part = s[space_pos:]

            if first_part not in memory:
                memory[first_part] = first_part in word_set

            if second_part == '':
                return memory[first_part]

            if memory[first_part]:
                if second_part not in memory:
                    memory[second_part] = self.wordBreakRec(second_part, word_set, memory)
                if memory[second_part]:
                    return True            

        return False


# catsandog
# cat sandog
# cat sand og
# cat sandog
# cats andog
# cats and og
# catsanddog
sol = Solution()
s = 'applepenapplepenapplepenpenpenappleapple'
wordDict = ['apple','pen']
print(sol.wordBreak(s, wordDict))
