class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mem = [None for _ in range(len(arr))]
        
        for i in range(len(arr)):
            is_odd = 1 if arr[i] % 2 == 1 else 0
            if i == 0:
                mem[i] = [is_odd, 1 - is_odd]
            else:
                mem[i] = [None, None]
                mem[i][0] = is_odd + mem[i-1][1] * is_odd + mem[i-1][0] * (1 - is_odd)
                mem[i][1] = (1 - is_odd) + mem[i-1][0] * is_odd + mem[i-1][1] * (1 - is_odd)
        
        # print(mem)
        return sum(map(lambda x: x[0], mem)) % 1000000007