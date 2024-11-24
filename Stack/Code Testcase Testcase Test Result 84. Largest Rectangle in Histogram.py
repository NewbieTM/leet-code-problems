#https://leetcode.com/problems/largest-rectangle-in-histogram/description/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_a = 0
        for i, el in enumerate(heights):
            start = i
            while stack and stack[-1][0] > el:
                height, index  = stack.pop()
                max_a = max(max_a, height * (i - index))
                start = index

            stack.append([el,start])
            
        for el,i in stack:
            area = el * (len(heights) - i)
            max_a = max(max_a, area)

        return max_a
