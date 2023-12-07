class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = list(num)
        while len(res) > 0 and int(res[-1]) % 2 == 0:
            res.pop()
        return ''.join(res)