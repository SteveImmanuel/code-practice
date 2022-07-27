# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List

class Solution:
    def perform_operation(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        else:
            is_neg = False
            if num1 < 0:
                is_neg = not is_neg
            if num2 < 0:
                is_neg = not is_neg
            res = abs(num1) // abs(num2)
            if is_neg:
                res *= -1
            return res
    
    def evalRPN(self, tokens: List[str]) -> int:
        mem_stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                mem_stack.append(int(token))
            else:
                num2 = mem_stack.pop()
                num1 = mem_stack.pop()
                # print(self.perform_operation(num1, num2, token))
                mem_stack.append(self.perform_operation(num1, num2, token))
        return mem_stack.pop()

sol = Solution()
tokens = ["2","1","+","3","*"]
print(sol.evalRPN(tokens))
