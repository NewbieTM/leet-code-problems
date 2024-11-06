#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum_of_el = numbers[l] + numbers[r]
            if sum_of_el > target:
                r-=1
            elif sum_of_el < target:
                l +=1
            else:
                return [l+1,r+1]



#Or (shorter version)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum_of_el = numbers[l] + numbers[r]
            r -= (sum_of_el > target)
            l += (sum_of_el < target)
            if sum_of_el == target:
                return [l+1,r+1]
