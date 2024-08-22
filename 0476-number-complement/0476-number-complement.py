class Solution:
    def findComplement(self, num: int) -> int:
        return int('0b'+''.join(map(str, map(int, [not x for x in map(int, list(bin(num)[2:]))]))), 2)