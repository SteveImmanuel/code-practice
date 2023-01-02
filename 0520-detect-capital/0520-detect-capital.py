class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up = word.upper()
        low = word.lower()
        capital = low.capitalize()
        
        val = True
        for i in range(len(word)):
            if word[i] != up[i]:
                val = False
                break
        
        if val:
            return True
        
        val = True
        for i in range(len(word)):
            if word[i] != low[i]:
                val = False
                break
        
        if val:
            return True
        
        val = True
        for i in range(len(word)):
            if word[i] != capital[i]:
                val = False
                break
        
        if val:
            return True