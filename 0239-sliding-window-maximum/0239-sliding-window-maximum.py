class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = [-num for num in nums[:k]]
        heapq.heapify(window)
        occ = Counter(window)
        answer = []
        for i in range(len(nums) - k + 1):
            while occ[window[0]] <= 0:
                heapq.heappop(window)
                
            answer.append(-window[0])
            
            if i + k < len(nums):
                occ[-nums[i]] -= 1
                occ[-nums[i + k]] += 1
                heapq.heappush(window, -nums[i + k])
        
        return answer