# https://leetcode.com/problems/basic-calculator-ii/
import string

# class Solution:
#     def calculate(self, s: str) -> int:
#         s = s.replace(' ', '')
#         num_arr = []
#         op_arr = []

#         num = ''
#         for char in s:
#             if char in string.digits:
#                 num += char
#             else:
#                 num_arr.append(int(num))
#                 num = ''
#                 op_arr.append(char)
#         num_arr.append(int(num))

#         idx = self.find(op_arr, ['*', '/'])
#         while idx!=-1:
#             res = self.calculate_res(num_arr[idx], num_arr[idx+1], op_arr[idx])
#             num_arr[idx] = res
#             num_arr.pop(idx+1)
#             op_arr.pop(idx)
#             idx = self.find(op_arr, ['*', '/'])
#         # print(num_arr, op_arr)

#         while len(op_arr) > 0:
#             op = op_arr.pop(0)
#             res = self.calculate_res(num_arr[0], num_arr[1], op)
#             num_arr[0] = res
#             num_arr.pop(1)
#         # print(num_arr, op_arr)
#         return num_arr[0]
        
        
#     def is_number(self, n):
#         for char in n:
#             if char not in string.digits:
#                 return False
#         return True
    
#     def find(self, arr, arr2):
#         i = 0
#         found = False
#         while i < len(arr) and not found:
#             if arr[i] in arr2:
#                 return i
#             i += 1
#         return -1
#     def calculate_res(self, left, right, op):
#         # print(left, right, op)
#         if op == '+':
#             return left + right
#         elif op == '-':
#             return left - right
#         elif op == '*':
#             return left * right
#         elif op == '/':
#             return left // right
class Solution:
    def calculate(self, s: str) -> int:
        n = 0 
        op = "+"
        st = []
        
        for ch in s + "+": 
            if ch.isdigit(): 
                n = 10 * n + int(ch) 
            elif ch in "+-*/": 
                if op == "+": 
                    st.append(n)
                elif op == "-": 
                    st.append(-n)
                elif op == "*": 
                    st.append(st.pop() * n)
                elif op == "/": 
                    st.append(int(st.pop() / n))
                op = ch 
                n = 0
        return sum(st)
sol = Solution()
s = " 1 / 2*3+6 "
s = "1-1+1"
# s = " 5 / 2 "
s='2+4/5'
print(sol.calculate(s))
