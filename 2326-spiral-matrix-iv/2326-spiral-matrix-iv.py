# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swap_direction(self, direction):
        if direction == (0, 1):
            return (1, 0)
        elif direction == (1, 0):
            return (0, -1)
        elif direction == (0, -1):
            return (-1, 0)
        elif direction == (-1, 0):
            return (0, 1)
        
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[None for _ in range(n)] for _ in range(m)]
        i = 0
        j = 0
        it = head
        cur_total = 0
        total = m * n
        direction = (0, 1)
        
        while cur_total < total:
            if it is not None:
                el = it.val
                it = it.next
            else:
                el = -1
            result[i][j] = el
            n_i = i + direction[0]
            n_j = j + direction[1]
            if n_i < 0 or n_i >= m or n_j < 0 or n_j >= n or result[n_i][n_j] is not None:
                direction = self.swap_direction(direction)
                i = i + direction[0]
                j = j + direction[1]
            else:
                i = n_i
                j = n_j
            cur_total += 1
        return result