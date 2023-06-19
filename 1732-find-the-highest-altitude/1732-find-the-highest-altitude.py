class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_max = 0
        cur_alt = 0
        for g in gain:
            cur_alt += g
            cur_max = max(cur_max, cur_alt)
        return cur_max