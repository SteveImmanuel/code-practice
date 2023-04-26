class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        digit = num % 9
        return digit if digit != 0 else 9