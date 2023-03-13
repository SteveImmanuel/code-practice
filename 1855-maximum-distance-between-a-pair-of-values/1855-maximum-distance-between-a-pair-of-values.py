class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_inv = nums2[::-1]
        max_dist = 0
        for i in range(len(nums1)):
            j = len(nums2) - bisect_left(nums2_inv, nums1[i]) - 1
            if j >= i:
                max_dist = max(max_dist, j - i)
                # print(i, j)
            # print(max_dist)
        return max_dist