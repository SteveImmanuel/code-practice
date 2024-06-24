class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        total = 0
        queue = deque([])
        for i in range(len(nums)):
            # print('before', i, nums, queue)
            
            # remove out of date barrier
            while len(queue) > 0 and queue[0] <= i: 
                queue.popleft()
            # print('    remove queue items', queue)
            # flip bit if odd
            is_flip = len(queue) % 2 == 1
            if is_flip: 
                nums[i] = 0 if nums[i] == 1 else 1
            # print(f'    after initial flip {is_flip}', nums[i])
            
            # flip and add barrier if the bit is 0
            if nums[i] == 0:
                total += 1
                queue.append(i + k)
                nums[i] = 1
            
            # print('after', i, nums, queue)
            # print()
        
        if len(queue) == 0 or (len(queue) == 1 and queue[0] == len(nums)):
            return total
        
        return -1