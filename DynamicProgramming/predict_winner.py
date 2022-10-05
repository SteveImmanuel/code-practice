# https://leetcode.com/problems/predict-the-winner/
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        mem = {}
        self.predict_winner_rec(nums, mem)
        print(mem)
        score1, score2 = mem[tuple(nums)]
        return score1 >= score2

    def predict_winner_rec(self, nums, mem):
        key = tuple(nums)
        if len(nums) == 1:
            mem[key] = (nums[0], 0)
        else:
            arr1 = nums[1:]
            arr2 = nums[:-1]
            key1 = tuple(arr1)
            key2 = tuple(arr2)

            current_point1 = nums[0]
            if key1 not in mem:
                self.predict_winner_rec(arr1, mem)
            fmove_score1, smove_score1 = mem[key1]
            current_point1 += smove_score1

            current_point2 = nums[-1]
            if key2 not in mem:
                self.predict_winner_rec(arr2, mem)
            fmove_score2, smove_score2 = mem[key2]
            current_point2 += smove_score2

            if current_point1 >= fmove_score1 and current_point2 >= fmove_score2:
                if current_point1 - fmove_score1 > current_point2 - fmove_score2:
                    mem[key] = (current_point1, fmove_score1)
                else:
                    mem[key] = (current_point2, fmove_score2)
            elif current_point1 >= fmove_score1:
                mem[key] = (current_point1, fmove_score1)
            elif current_point2 >= fmove_score2:
                mem[key] = (current_point2, fmove_score2)
            else:
                if fmove_score1 - current_point1 > fmove_score2 - current_point2:
                    mem[key] = (current_point2, fmove_score2)
                else:
                    mem[key] = (current_point1, fmove_score1)

            



sol = Solution()
nums = [1,5,2,7]*5
print(sol.PredictTheWinner(nums))