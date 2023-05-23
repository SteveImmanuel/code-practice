class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors_fhalf = [1]
        factors_shalf = deque([n])
        
        for i in range(2, int(n ** 0.5) + 1):
            div, mod = divmod(n, i)
            if mod == 0:
                factors_fhalf.append(i)
                if div != i:
                    factors_shalf.appendleft(div)
            
            if len(factors_fhalf) == k:
                return factors_fhalf[-1]
        
        factors = factors_fhalf + list(factors_shalf)
        if len(factors) >= k:
            return factors[k - 1]
        return -1
                    