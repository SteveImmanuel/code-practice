class Solution:
    def is_divisible(self, str1, str2):
        #str2 <= str1
        if len(str1) % len(str2) != 0:
            return False
        i = 0
        for char in str1:
            if char != str2[i]:
                return False
            i = (i + 1) % len(str2)
        return True
        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pivot = str1 if len(str1) < len(str2) else str2
        for i in range(len(pivot), 0, -1):
            divisor = pivot[:i]
            if self.is_divisible(str1, divisor) and self.is_divisible(str2, divisor):
                return divisor
        return ''