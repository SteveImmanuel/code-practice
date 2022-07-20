# https://leetcode.com/problems/number-of-matching-subsequences/
from typing import List

class Solution:
    def is_match(self, s, subseq):
        i = 0
        for char in s:
            if char == subseq[i]:
                i += 1
            if i == len(subseq):
                break
        
        return i == len(subseq)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        total = 0
        mem = {}
        for word in words:
            if not word in mem:
                mem[word] = self.is_match(s, word)
            
            if mem[word]:
                total += 1
        return total

sol = Solution()
s = "abcde"
words = ["a","bb","acd","ace"]
# s = "dsahjpjauf"
# words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
print(sol.numMatchingSubseq(s, words))