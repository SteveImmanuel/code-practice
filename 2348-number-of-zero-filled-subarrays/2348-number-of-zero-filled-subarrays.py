class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        empty_intervals = []
        cur_interval = [None, None]
        for i, num in enumerate(nums):
            if num != 0:
                if cur_interval[0] is not None:
                    empty_intervals.append(cur_interval)
                cur_interval = [None, None]
            else:
                if cur_interval[0] is None:
                    cur_interval = [i, i]
                else:
                    cur_interval[1] = i
        if cur_interval[0] is not None:
            empty_intervals.append(cur_interval)
        
        total = 0
        for start, end in empty_intervals:
            length = end - start + 1
            total += ((length) * (length + 1)) // 2
        return total