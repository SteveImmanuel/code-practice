class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[None for _ in range(n)] for _ in range(m)]
        deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(m):
            for j in range(n):
                total = 0
                n_valid = 0
                for di, dj in deltas:
                    if i + di < 0 or i + di >= m or j+ dj < 0 or j + dj >= n:
                        continue
                    n_valid += 1
                    total += img[i+di][j+dj]
                res[i][j] = total // n_valid
        return res
                