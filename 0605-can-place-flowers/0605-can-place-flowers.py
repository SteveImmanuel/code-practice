class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_intervals = []
        cur_interval = [None, None]
        for i, num in enumerate(flowerbed):
            if num == 1:
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
        
        total_possible = 0
        for start, end in empty_intervals:
            if start != 0:
                start += 1
            if end != len(flowerbed) - 1:
                end -= 1
            
            if end < start:
                continue
            
            empty_slots = end - start + 1
            if empty_slots % 2 == 1:
                empty_slots += 1
            total_possible += empty_slots // 2
        # print(total_possible)
        return n <= total_possible