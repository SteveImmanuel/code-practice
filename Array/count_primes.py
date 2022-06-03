# https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * (n)
        i = 2

        while i * i < n:
            if (not is_prime[i]):
                i += 1
                continue

            for j in range(i * i, n, i):
                is_prime[j] = False 
            
            i += 1

        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
        return count

sol = Solution()
print(sol.countPrimes(20))
# print(sol.isPrime(19*19, [2,3,5,7,11,13,17,19]))