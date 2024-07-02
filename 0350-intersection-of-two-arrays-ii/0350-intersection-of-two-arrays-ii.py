class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        o1 = Counter(nums1)
        o2 = Counter(nums2)
        i = set(o1.keys()).intersection(o2.keys())
        result = []
        for x in i:
            result += [x] * min(o1[x], o2[x])
        return result