class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        num_dict = defaultdict(list)
        for i, num in enumerate(nums):
            num_dict[num].append(i)
        # print(nums)
        
        visited = [False] * len(nums)
        max_length = -1
        for i in range(len(nums)):
            if visited[i]:
                continue
                
            cur_length = 0
            cur_num = nums[i]
            while cur_num in num_dict:
                cur_length += 1
                for x in num_dict[cur_num]:
                    visited[x] = True
                cur_num *= cur_num
            
            if cur_length > 1:
                max_length = max(max_length, cur_length)
                
            # print(visited)
        
        return max_length
            