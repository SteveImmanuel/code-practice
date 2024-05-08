class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n >= 2:
            return 0.5
        return 1