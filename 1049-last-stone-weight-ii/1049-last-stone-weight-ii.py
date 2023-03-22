class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        mem = [[None for _ in range((total//2) + 1)] for _ in range(len(stones) + 1)]
        
        for i in range(len(mem)):
            for j in range(len(mem[i])):
                if i == 0 or j == 0:
                    mem[i][j] = 0
                else:
                    mem[i][j] = mem[i-1][j]
                    if j >= stones[i-1]:
                        mem[i][j] = max(mem[i][j], stones[i-1] + mem[i-1][j - stones[i-1]])
        
        # print(total)
        # print(mem[len(stones)][total // 2])
        return abs(total - 2 * mem[len(stones)][total // 2])
                        