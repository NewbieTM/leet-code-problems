#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot():
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def binary_search(sorted_half_of_nums):
            l,r = 0, len(sorted_half_of_nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if sorted_half_of_nums[mid] > target:
                    r = mid - 1
                elif sorted_half_of_nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return -1

        pivot_entry_to_right = find_pivot() # find the pivot index
        if pivot_entry_to_right != 0: # check if it even rotated somehow
            if target < nums[0]: # select a left or a right part from pivot index to check
                answer = binary_search(nums[pivot_entry_to_right:])
                return pivot_entry_to_right + answer if answer != -1 else -1
            else:
                answer = binary_search(nums[:pivot_entry_to_right])
                return answer if answer != -1 else -1
        else:
            return binary_search(nums)
