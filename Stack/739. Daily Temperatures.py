#https://leetcode.com/problems/daily-temperatures/description/

#Solution is a Descending order (Monotonic) stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index

            stack.append(i)
            
            
        return res 
