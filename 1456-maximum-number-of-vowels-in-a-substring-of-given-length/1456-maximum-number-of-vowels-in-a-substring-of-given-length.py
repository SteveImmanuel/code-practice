class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur_vowel = 0
        
        for i in range(k):
            if self.is_vowel(s[i]):
                cur_vowel += 1

        max_vowel = cur_vowel
        for i in range(1, len(s) - k + 1):
            if self.is_vowel(s[i - 1]):
                cur_vowel -= 1
            if self.is_vowel(s[i + k - 1]):
                cur_vowel += 1
            max_vowel = max(cur_vowel, max_vowel)
            
        return max_vowel
            
        
    def is_vowel(self, char):
        return char in ['a', 'i', 'u', 'e', 'o']