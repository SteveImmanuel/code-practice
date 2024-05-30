class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [None] * len(arr)
        cur = 0
        for i, x in enumerate(arr):
            cur ^= x
            prefix_xor[i] = cur
        
        total = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    a = prefix_xor[j - 1]
                    if i > 0:
                        a ^= prefix_xor[i - 1]
                    b = prefix_xor[k] ^ prefix_xor[j - 1]
                    if a == b:
                        total += 1
        return total