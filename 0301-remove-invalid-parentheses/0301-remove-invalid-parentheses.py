class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = set()
        self.traverse(s, 0, 0, [], result)
        # print(result)
        result = list(map(lambda x: (len(x), x), result))
        max_len = 0
        for item in result:
            max_len = max(max_len, item[0])
        result = filter(lambda x: x[0] == max_len, result)
        result = list(map(lambda x: x[1], result))
        return result
    
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         result = []
        
#         n = len(s)
#         max_num = 2 ** n
#         char_mask = []
#         for i in range(len(s)):
#             if s[i] not in ['(', ')']:
#                 char_mask.append('1')
#             else:
#                 char_mask.append('0')
#         if len(char_mask) == 0:
#             char_mask = 0
#         else:
#             char_mask = int('0b' + ''.join(char_mask), 2)
        
#         result = []
#         for mask in range(max_num):
#             cur_mask = mask | char_mask
#             cur_string = self.create_string(s, cur_mask)
#             if cur_string != -1:
#                 result.append(cur_string)
#         result = list(map(lambda x: (len(x), ''.join(x)), result))
#         max_len = 0
#         for item in result:
#             max_len = max(max_len, item[0])
#         result = filter(lambda x: x[0] == max_len, result)
#         result = list(map(lambda x: x[1], result))
#         result = list(set(result))
#         return result
    
#     def create_string_and_check(self, s, cur_mask):
#         result = []
#         stack = []
#         mask = bin(cur_mask)[2:]
#         mask = '0' * (len(s) - len(mask)) + mask
#         # print(mask)
#         for i in range(len(s)):
#             if mask[i] == '1':
#                 result.append(s[i])
#                 if s[i] == '(':
#                     stack.append(s[i])
#                 elif s[i] == ')':
#                     if len(stack) <= 0:
#                         return -1
#                     else:
#                         prev = stack.pop()
#                         if prev != '(':
#                             return -1
#         return result
        
#     def create_string(self, s, cur_mask):
#         result = []
#         mask = bin(cur_mask)[2:]
#         mask = '0' * (len(s) - len(mask)) + mask
#         # print(mask)
#         for i in range(len(s)):
#             if mask[i] == '1':
#                 result.append(s[i])
#         return result
    
    def traverse(self, s, cur_idx, budget, cur_result, result):
        # print(s, cur_idx, budget, cur_result)
        if budget < 0:
            return
        if cur_idx == len(s):
            if budget == 0:
                temp = ''.join(cur_result)
                result.add(temp)
            return
        
        len_cur_result = len(cur_result)
        
        #case use
        cur_result = cur_result[:len_cur_result]
        cur_result.append(s[cur_idx])
        if s[cur_idx] == '(':
            self.traverse(s, cur_idx + 1, budget + 1, cur_result, result)
        elif s[cur_idx] == ')':
            self.traverse(s, cur_idx + 1, budget - 1, cur_result, result)
        else:
            self.traverse(s, cur_idx + 1, budget, cur_result, result)
            
            
        #case remove
        cur_result = cur_result[:len_cur_result]
        if s[cur_idx] in ['(', ')']:
            self.traverse(s, cur_idx + 1, budget, cur_result, result)
        
        
#     def is_valid(self, s):
#         stack = []
#         for char in s:
#             if char == '(':
#                 stack.append(char)
#             elif char == ')':
#                 if len(stack) <= 0:
#                     return False
#                 else:
#                     prev = stack.pop()
#                     if prev != '(':
#                         return False
#         return len(stack) == 0