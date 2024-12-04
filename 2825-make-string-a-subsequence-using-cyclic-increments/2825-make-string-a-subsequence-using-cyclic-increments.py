class Solution:
    def next_char(self, char):
        return chr(((ord(char) - 97 + 1) % 26) + 97)
    
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx1 = 0
        idx2 = 0
        while idx1 < len(str1) and idx2 < len(str2):
            if str1[idx1] == str2[idx2] or self.next_char(str1[idx1]) == str2[idx2]:
                idx2 += 1
            idx1 += 1
        
        return idx2 >= len(str2)