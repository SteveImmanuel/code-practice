class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs_sort = sorted(pairs, key=lambda x:(x[0], x[1]))
        mem = [1] * len(pairs_sort)
        for i in range(len(pairs_sort)):
            for j in range(i):
                if pairs_sort[i][0] > pairs_sort[j][1]:
                    mem[i] = max(mem[i], mem[j] + 1)
        
        return max(mem)
