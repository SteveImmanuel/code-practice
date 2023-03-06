class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start_num = 0
        total = 0
        
        for end_num in arr:
            last_total = total
            total += end_num - start_num - 1
            if total >= k:
                return start_num + k - last_total
            start_num = end_num
        
        return start_num + k - total