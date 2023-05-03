class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        intersection = set_1.intersection(set_2)
        return [list(set_1.difference(intersection)), list(set_2.difference(intersection))]