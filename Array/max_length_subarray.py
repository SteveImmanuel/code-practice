# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
from typing import List
class Solution:
    # Works on same length only
    # def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    #     max_length = 0
    #     for i in range(len(nums1)):
    #         current_length = 0
    #         ptr1 = (len(nums1) - 1) - i
    #         ptr2 = 0
    #         current_streak = 0
    #         streak = False
    #         while ptr2 < i + 1:
    #             # print(nums1[ptr1], nums2[ptr2], ptr1, ptr2, streak, current_streak)
    #             if nums1[ptr1] == nums2[ptr2] and (streak or current_streak == 0):
    #                 streak = True
    #                 current_streak += 1
    #             else:
    #                 streak = False
    #                 current_length = max(current_length, current_streak)
    #                 current_streak = 0
    #             ptr1 += 1
    #             ptr2 += 1
    #         current_length = max(current_length, current_streak)
    #         max_length = max(current_length, max_length)
    #         # print()

    #     for i in range(len(nums1)):
    #         current_length = 0
    #         ptr1 = (len(nums1) - 1) - i
    #         ptr2 = 0
    #         current_streak = 0
    #         streak = False
    #         while ptr2 < i + 1:
    #             # print(nums2[ptr1], nums1[ptr2], ptr1, ptr2, streak, current_streak)
    #             if nums2[ptr1] == nums1[ptr2] and (streak or current_streak == 0):
    #                 streak = True
    #                 current_streak += 1
    #             else:
    #                 streak = False
    #                 current_length = max(current_length, current_streak)
    #                 current_streak = 0
    #             ptr1 += 1
    #             ptr2 += 1
    #         current_length = max(current_length, current_streak)
    #         max_length = max(current_length, max_length)
    #         # print()
    #     return max_length

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2):
            small_arr = nums1
            long_arr = nums2
        else:
            small_arr = nums2
            long_arr = nums1
        
        max_length = 0
        for i in range(len(nums1) + len(nums2)):
            ptr_small = max(0, (len(small_arr) - 1) - i)
            ptr_long = max(0, i - (len(long_arr) - 1))
            current_length = 0
            current_streak = 0
            streak = False

            for _ in range(min(len(small_arr) - ptr_small, len(long_arr) - ptr_long)):
                # print(small_arr[ptr_small], long_arr[ptr_long], ptr_small, ptr_long, streak, current_streak)
                if long_arr[ptr_long] == small_arr[ptr_small] and (streak or current_streak == 0):
                    streak = True
                    current_streak += 1
                else:
                    streak = False
                    current_length = max(current_length, current_streak)
                    current_streak = 0
                ptr_small += 1
                ptr_long += 1
            # print()
            
            current_length = max(current_length, current_streak)
            max_length = max(current_length, max_length)
        return max_length
                    

sol = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
nums1 = [0,0,0,0,1]
nums2 = [1,0,0,0,0]
nums1 = [1,2,1,1,1,1,2,3,4,5] * 100
nums2 = [1,5,1,2,3,1,2,3,4,5] * 100
nums1=[1,2,3,2,1]
nums2=[3,2,1,4]
print(sol.findLength(nums1, nums2))