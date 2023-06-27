class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        checked_idx = set([])
        result = []
        while len(heap) > 0 and len(result) < k:
            cur_sum, i, j = heappop(heap)
            if (i, j) in checked_idx:
                continue
            checked_idx.add((i, j))
            result.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
            if j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
            # print(heap, result)
        return result
                
            