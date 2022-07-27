# https://leetcode.com/problems/spiral-matrix/

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        has_visited = []
        for i in range(len(matrix)):
            has_visited.append([False] * len(matrix[i]))

        i,j = 0,0
        can_move = True
        row = len(matrix)
        col = len(matrix[0])
        res = []

        while can_move:
            # move right
            if i < row and j < col and not has_visited[i][j]:
                while j < col and not has_visited[i][j] and can_move:
                    res.append(matrix[i][j])
                    has_visited[i][j] = True
                    j += 1
                j -= 1
            else:
                can_move = False
            i += 1

            # move down
            # print(i, j, row,col)
            if i < row and j < col and not has_visited[i][j]:
                while i < row and not has_visited[i][j] and can_move:
                    res.append(matrix[i][j])
                    has_visited[i][j] = True
                    i += 1
                i -= 1
            else:
                can_move = False
            j -= 1

            # move left
            if i < row and j < col and not has_visited[i][j]:
                while j > -1 and not has_visited[i][j] and can_move:
                    res.append(matrix[i][j])
                    has_visited[i][j] = True
                    j -= 1
                j += 1
            else:
                can_move = False
            i -= 1

            # move up
            if i < row and j < col and not has_visited[i][j]:
                while i > -1 and not has_visited[i][j] and can_move:
                    res.append(matrix[i][j])
                    has_visited[i][j] = True
                    i -= 1
                i += 1
            else:
                can_move = False
            j += 1

        return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,3,4],[5,6,7,8]]
sol = Solution()
print(sol.spiralOrder(matrix))