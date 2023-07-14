class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mem = defaultdict(int)
        for i in range(len(arr)):
            if i == 0 or arr[i] - difference not in mem:
                mem[arr[i]] = 1
            else:            
                mem[arr[i]] = max(mem[i], 1 + mem[arr[i] - difference])
        # print(mem)
        return max(list(mem.values()))
                    