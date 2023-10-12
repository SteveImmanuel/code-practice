class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        mem = [[0 for _ in range(m)] for _ in range(n)]
        
        max_by_col = [0 for _ in range(m)]
        for i in range(n):
            cur_max = 0
            last_max_by_col = max_by_col[:]
            for j in range(m):
                if i == 0:
                    mem[i][j] = 1 if nums2[i] == nums1[j] else 0
                else:
                    prev_max = 0
                    if j > 0:
                        prev_max = last_max_by_col[j - 1]
                    mem[i][j] = 1 + prev_max if nums2[i] == nums1[j] else prev_max
                    
                cur_max = max(cur_max, mem[i][j])
                max_by_col[j] = max(max_by_col[j], cur_max)
            last_max_by_col = max_by_col
        # for x in mem:
        #     print(x)
        # print(max_by_col)
        return max(max_by_col)