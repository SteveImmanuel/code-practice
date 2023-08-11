class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        idx = defaultdict(list)
        for i in range(len(nums)):
            idx[nums[i]].append(i)
            
        global_min = float('inf')
        for key in idx.keys():
            if len(idx[key]) == 1:
                cur_min = len(nums) // 2
            else:
                cur_min = 0
                for i in range(len(idx[key])):
                    if i < len(idx[key]) - 1:
                        cur_min = max(cur_min, (idx[key][i+1] - idx[key][i]) // 2)
                    else:
                        cur_min = max(cur_min, (idx[key][0] + len(nums) - idx[key][i]) // 2)
            global_min = min(global_min, cur_min)
            # print(key, cur_min)

            
        return global_min
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#     def minimumSeconds(self, nums: List[int]) -> int:
#         target_candidate = set(nums)
#         cur_min = float('inf')
        
#         for target in target_candidate:
#             remaining = []
#             counter = 0
#             for num in nums:
#                 # print(counter, num, remaining)
#                 if num != target:
#                     counter += 1
#                 else:
#                     if counter != 0:
#                         remaining.append(counter)
#                         counter = 0
#             if counter != 0:
#                 remaining.append(counter)
#                 counter = 0

#             if len(remaining) == 0:
#                 return 0

#             if nums[0] != target and nums[-1] != target:
#                 remaining[0] += remaining.pop()
#             # print(target, remaining)
#             cur_min = min(cur_min, (max(remaining) + 1) // 2)
#         return cur_min
    
#     def minimumSeconds(self, nums: List[int]) -> int:
#         sorted_target = self.get_target(nums)
#         cur_min = float('inf')
        
#         target_candidate = [sorted_target[0][0]]
#         max_influence = sorted_target[0][1]
#         i = 1
#         while i < len(sorted_target) and sorted_target[i][1] == max_influence and max_influence != 3:
#             target_candidate.append(sorted_target[i][0])
#             i += 1
#         print(target_candidate)
#         for target in target_candidate:
#             remaining = []
#             counter = 0
#             for num in nums:
#                 # print(counter, num, remaining)
#                 if num != target:
#                     counter += 1
#                 else:
#                     if counter != 0:
#                         remaining.append(counter)
#                         counter = 0
#             if counter != 0:
#                 remaining.append(counter)
#                 counter = 0

#             if len(remaining) == 0:
#                 return 0

#             if nums[0] != target and nums[-1] != target:
#                 remaining[0] += remaining.pop()
#             print(target, remaining)
#             cur_min = min(cur_min, (max(remaining) + 1) // 2)
#         return cur_min
    
#     def get_target(self, nums):
#         idx = defaultdict(list)
#         for i in range(len(nums)):
#             idx[nums[i]].append([i-1, i+1])
            
#         for key in idx.keys():
#             i = 0
#             while i < len(idx[key]) - 1:
#                 if idx[key][i][1] >= idx[key][i+1][0]:
#                     idx[key][i][1] = idx[key][i+1][1]
#                     idx[key].pop(i+1)
#                 else:
#                     i += 1
                    
#             if len(idx[key]) > 1 and idx[key][-1][1] >= idx[key][0][0] + len(nums):
#                 idx[key][0][0] = idx[key][-1][0]
#                 idx[key][0][1] = idx[key][0][1] + len(nums)
#                 idx[key].pop()
            
#             print(key, idx[key])
            
            
#             total_influence = 0
#             for i in range(len(idx[key])):
#                 total_influence += idx[key][i][1] - idx[key][i][0] + 1
#             idx[key] = total_influence
        
#         sorted_target = sorted(list(idx.items()), key=lambda x:x[1], reverse=True)
#         print(sorted_target)
#         return sorted_target
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        