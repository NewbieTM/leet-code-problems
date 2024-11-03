#https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_l = 0
        
        for el in s:
            if el-1 not in s:
                length = 0
                while el + length in s:
                    length+=1
                    
                max_l = max(max_l, length)
        
        return max_l