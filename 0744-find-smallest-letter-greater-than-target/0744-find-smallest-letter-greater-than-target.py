class Solution:
    # Bruteforce O(n)
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     letter = None
    #     for i in range(len(letters)):
    #         diff = ord(letters[i]) - ord(target)
    #         if diff > 0 and (letter is None or diff < ord(letter) - ord(target)):
    #             letter = letters[i]
    #     if letter is None:
    #         return letters[0]
    #     return letter
    
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = self.bisect_right(letters, target)
        if idx >= len(letters):
            return letters[0]
        return letters[idx]
        
    def bisect_right(self, arr, target):
        l = 0
        r = len(arr)
        
        while l < r:
            m = (l + r) // 2
            if ord(arr[m]) <= ord(target):
                l = m + 1
            else:
                r = m
        return l
                