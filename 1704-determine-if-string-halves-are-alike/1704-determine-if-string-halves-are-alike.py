class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half_idx = len(s) // 2
        total_vowel = 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        for i in range(half_idx):
            if s[i] in vowels:
                total_vowel += 1
                
        for i in range(half_idx, len(s)):
            if s[i] in vowels:
                total_vowel -= 1
        
        return total_vowel == 0
                
        