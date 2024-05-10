class Solution:
    # def get_kth_number(self, heap, k):
    #     print(heap, k)
    #     buffer = []
    #     while k > 0:
    #         res = heapq.heappop(heap)
    #         buffer.append(res)
    #         k -= 1
    #     while len(buffer) > 0:
    #         heapq.heappush(heap, buffer.pop())
    #     return res
            
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         heap = []
#         for d_idx in range(len(arr) - 1, 0, -1):
#             found = False
#             for n_idx in range(d_idx):
#                 heapq.heappush(heap, (arr[n_idx] / arr[d_idx], arr[n_idx], arr[d_idx]))
        
        
#         while k > 0:
#             res = heapq.heappop(heap)
#             k -= 1
#         return [res[1], res[2]]
    
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = [(arr[0] / arr[i], arr[0], arr[i], 0, i) for i in range(len(arr) - 1, 0, -1)]
        heapq.heapify(heap)
        
        res = []
        while len(res) < k:
            _, n, d, n_idx, d_idx = heapq.heappop(heap)
            res.append([n, d])
            if n_idx + 1 < d_idx:
                heapq.heappush(heap, (arr[n_idx+1]/ arr[d_idx], arr[n_idx+1], arr[d_idx], n_idx+1, d_idx))
        
        return res[-1]
            
