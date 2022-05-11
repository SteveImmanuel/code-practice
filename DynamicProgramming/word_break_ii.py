# https://leetcode.com/problems/word-break-ii/
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memory = {}
        res = self.wordBreakRec(s, word_set, memory)
        print(memory)
        return res

    def wordBreakRec(self, s, word_set, memory):
        res = []

        for space_pos in range(1, len(s)+1):
            first_part = s[:space_pos]
            second_part = s[space_pos:]

            if first_part not in memory and first_part in word_set:
                memory[first_part] = [first_part]


            if first_part in word_set:
                if second_part == '':
                    res.append(first_part)
                    break

                if second_part not in memory:
                    memory[second_part] = self.wordBreakRec(second_part, word_set, memory)
                if len(memory[second_part]) > 0:
                    for part in memory[second_part]:
                        res.append(f'{first_part} {part}')

        return res


sol = Solution()
s = 'pineapplepenapple'
wordDict = ["apple","pen","applepen","pine","pineapple"]
print(sol.wordBreak(s, wordDict))
