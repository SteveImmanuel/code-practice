class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        memory = [None] * len(nums)

        for i in range(0, len(nums)):
            if i == 0:
                memory[i] = (1, 1)
            else:
                max_length_before = [0, 1]
                for j in range(i):
                    if nums[j] < nums[i]:
                        if memory[j][0] > max_length_before[0]:
                            max_length_before = list(memory[j])
                        elif memory[j][0] == max_length_before[0]:
                            max_length_before[1] += memory[j][1]
                memory[i] = (1 + max_length_before[0], max_length_before[1])
        total = 0
        max_occ = 0
        for i in range(len(memory)):
            if memory[i][0] > max_occ:
                total = memory[i][1]
                max_occ = memory[i][0]
            elif memory[i][0] == max_occ:
                total += memory[i][1]
        return total