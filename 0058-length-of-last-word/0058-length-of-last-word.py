class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(lambda x: len(x) > 0, s.split(' ')))[-1])