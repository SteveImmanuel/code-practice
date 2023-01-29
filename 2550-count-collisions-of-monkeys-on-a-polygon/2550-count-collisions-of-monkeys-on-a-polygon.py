class Solution:
    def monkeyMove(self, n: int) -> int:
        base = 2
        exponent = n
        modulus = 1000000007

        res = 1
        while exponent > 0:
            if exponent % 2 == 1:
                res = (res * base) % modulus
            base = (base * base) % modulus
            exponent = exponent // 2
        
        
        return (res - 2) % 1000000007