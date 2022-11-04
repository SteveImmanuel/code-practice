class Solution:
    def reverseVowels(self, s: str) -> str:
        res = []
        vowels = []
        for char in s:
            if char in 'aiueoAIUEO':
                vowels.append(char)
                res.append(None)
            else:
                res.append(char)
        
        vowels = vowels[::-1]
        j = 0
        for i in range(len(res)):
            if res[i] is None:
                res[i] = vowels[j]
                j += 1
        return ''.join(res)