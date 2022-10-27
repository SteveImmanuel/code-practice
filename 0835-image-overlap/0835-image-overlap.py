class Solution:
    def generate_patch(self, img1):
        n = len(img1)

        start_idx = [0] * n + [i for i in range(1, n)]
        end_idx = [i for i in range(n)] + [n-1 for _ in range(1, n)]
        for start_row, end_row in zip(start_idx, end_idx):
            for start_col, end_col in zip(start_idx, end_idx):
                yield (start_row, start_col), (end_row, end_col)
    
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        largest_overlap = 0
        for patch in self.generate_patch(img1):
            (i,j), (k,l) = patch
            total_col = l - j + 1
            total_row = k - i + 1
            i2 = n - 1 - k
            j2 = n - 1 - l
            # k2 = n - 1 - i
            # l2 = n - 1 - j
            total_one = 0
            # print(patch, largest_overlap, total_row, total_col, i2, j2)
            for x in range(total_row):
                for y in range(total_col):
                    if img1[i + x][j + y] == img2[i2 + x][j2 + y] == 1:
                        total_one += 1
            largest_overlap = max(largest_overlap, total_one)
        return largest_overlap