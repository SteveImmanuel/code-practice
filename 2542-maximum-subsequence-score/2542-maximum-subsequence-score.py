class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(num1, num2) for num1, num2 in zip(nums1, nums2)]
        pairs.sort(key=lambda x:(-x[1],-x[0]))
        
        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)
        
        max_score = top_k_sum * pairs[k-1][1]
        for i in range(k, len(pairs)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])
            
            max_score = max(max_score, top_k_sum * pairs[i][1])
        
        return max_score
            