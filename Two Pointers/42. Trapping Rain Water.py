#https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[0], height[-1]
        area = 0
        while l < r:
            if max_l <= max_r:
                l+=1
                if max_l - height[l] > 0:
                    area += max_l - height[l]
            else:
                r-=1
                if max_r - height[r] > 0:
                    area += max_r - height[r]
                
            
            max_l, max_r = max(max_l,height[l]), max(max_r,height[r]) 
        
        return area
