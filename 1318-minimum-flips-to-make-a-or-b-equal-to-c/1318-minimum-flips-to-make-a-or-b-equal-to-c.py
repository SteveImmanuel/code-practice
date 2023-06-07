class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        max_num = max(a, b, c)
        flip = 0
        while max_num > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            
            if bit_a | bit_b != bit_c:
                if bit_c == 0:
                    flip += (bit_a & 1) + (bit_b & 1)
                else:
                    flip += 1
            # print(bit_a, bit_b, bit_c, flip)
            a = a >> 1
            b = b >> 1
            c = c >> 1
            max_num = max_num >> 1
        # print()
        return flip