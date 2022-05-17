# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        memory = [1] + [0] * n

        for i in range(1, n + 1):
            if i == 1:
                memory[i] = i
            else:
                for j in range(i):
                    left_nodes = j
                    right_nodes = (i - 1) - j
                    memory[i] += memory[left_nodes] * memory[right_nodes]
        return memory[-1]


sol = Solution()
n = 8
print(sol.numTrees(n))