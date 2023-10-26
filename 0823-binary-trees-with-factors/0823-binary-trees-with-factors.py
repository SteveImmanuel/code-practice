class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 1000000007
        arr.sort()
        mem = defaultdict(int)
        for i in range(len(arr)):
            self.calculate(i, arr, mem)
        total = sum(mem.values()) % MOD
        return total
            
    def calculate(self, idx, arr, mem):
        MOD = 1000000007
        if arr[idx] not in mem:
            total = 1
            for i in range(idx):
                div, mod = divmod(arr[idx], arr[i])
                if mod == 0:
                    variants = mem[div] * mem[arr[i]]
                    total += variants % MOD
            mem[arr[idx]] = total % MOD
        return mem[arr[idx]]