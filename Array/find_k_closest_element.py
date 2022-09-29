# https://leetcode.com/problems/find-k-closest-elements/
from typing import List
from collections import deque

class Solution:
    def bin_search(self, arr, val):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == val:
                return mid, True
            elif arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1
        return mid, False

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()
        
        small_idx, found = self.bin_search(arr, x)
        if not found and len(arr) % 2 == 0:
            small_idx -= 1

        big_idx = small_idx + 1
        print(small_idx)
        i = 0
        while i < k:
            if small_idx >= 0 and big_idx <= len(arr) - 1:
                if abs(arr[small_idx] - x) <= abs(arr[big_idx] - x):
                    res.appendleft(arr[small_idx])
                    small_idx -= 1
                else: # abs(arr[small_idx] - x) > abs(arr[big_idx] - x)
                    res.append(arr[big_idx])
                    big_idx += 1
            elif small_idx >= 0:
                res.appendleft(arr[small_idx])
                small_idx -= 1
            else:
                res.append(arr[big_idx])
                big_idx += 1

            i += 1
        return list(res)


arr = [1,3]
k = 2
x = 2
sol = Solution()
print(sol.findClosestElements(arr, k, x))