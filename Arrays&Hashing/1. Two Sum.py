#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,el in enumerate(nums):
            if target - el in d:
                return [d[target - el],i]
            d[el] = i + d.get(el,0)