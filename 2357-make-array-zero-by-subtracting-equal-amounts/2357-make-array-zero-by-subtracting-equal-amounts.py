class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
#         heap_nums = nums
#         heapq.heapify(heap_nums)
        
#         total_op = 0
#         smallest_el = heapq.heappop(heap_nums)
#         while smallest_el != 0:
#             total_op += 1

        num_set = set(nums)
        if 0 in num_set:
            num_set.remove(0)
        return len(num_set)