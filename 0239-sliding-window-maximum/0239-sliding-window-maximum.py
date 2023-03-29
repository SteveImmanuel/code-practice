class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = [-num for num in nums[:k]]
        heapq.heapify(window)
        occ_dict = Counter(window)
        # print(occ_dict)
        # print(window)
        res = []
        for i in range(len(nums) - k + 1):
            while occ_dict[window[0]] <= 0:
                heapq.heappop(window)
            # print(window[0], occ_dict, window)
            res.append(-window[0])
            if i < len(nums) - k:
                occ_dict[-nums[i]] -= 1
                occ_dict[-nums[i + k]] += 1
                heapq.heappush(window, -nums[i + k])
        
        return res
                
                
        
        