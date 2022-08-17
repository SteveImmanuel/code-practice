# https://leetcode.com/problems/unique-morse-code-words/
from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {
            'a':".-",
            'b':"-...",
            'c':"-.-.",
            'd':"-..",
            'e':".",
            'f':"..-.",
            'g':"--.",
            'h':"....",
            'i':"..",
            'j':".---",
            'k':"-.-",
            'l':".-..",
            'm':"--",
            'n':"-.",
            'o':"---",
            'p':".--.",
            'q':"--.-",
            'r':".-.",
            's':"...",
            't':"-",
            'u':"..-",
            'v':"...-",
            'w':".--",
            'x':"-..-",
            'y':"-.--",
            'z':"--..",
        }
        res = set()
        for word in words:
            morse = ''
            for char in word:
                morse += morse_dict[char]
            res.add(morse)
        # print(res)
        return len(res)

sol = Solution()
words = ["a"]
print(sol.uniqueMorseRepresentations(words))