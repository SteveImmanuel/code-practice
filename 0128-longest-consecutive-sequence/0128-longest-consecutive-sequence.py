class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        
        while len(num_set) > 0:
            cur_len = 1
            num = num_set.pop()
            up_num = num + 1
            while up_num in num_set:
                num_set.remove(up_num)
                up_num += 1
                cur_len += 1
            down_num = num - 1
            while down_num in num_set:
                num_set.remove(down_num)
                down_num -= 1
                cur_len += 1
            max_len = max(max_len, cur_len)
                
        return max_len