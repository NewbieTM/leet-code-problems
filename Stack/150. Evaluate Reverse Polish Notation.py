#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opperations = [ '+', '-', '*', '/']
        for el in tokens:
            if el in opperations:
                if el == '+':
                    res = stack[-1] + stack[-2]
                if el == '-':
                    res = stack[-2] - stack[-1]
                if el == '*':
                    res = stack[-1] * stack[-2]
                if el == '/':
                    res = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res) 
            else:
                stack.append(int(el))
           
            
        return stack[-1]
