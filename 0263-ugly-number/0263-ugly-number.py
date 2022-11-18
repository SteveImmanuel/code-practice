class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
    
        prime = [2,3,5]
        prime_idx = 0
        
        while n > 1:
            if n % prime[prime_idx] == 0:
                n = n // prime[prime_idx]
            else:
                if prime_idx < len(prime) - 1:
                    prime_idx += 1
                else:
                    return False

        return True