#https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = { ')':'(', ']':'[', '}':'{'}
        for el in s:
            if el in ['(', '[', '{']:
                stack.append(el)
            else:
                if stack and d[el] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
