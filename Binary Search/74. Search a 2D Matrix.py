#https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        left, right = 0, len(matrix) * width - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // width, mid % width
            
            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right  = mid - 1
            else:
                return True

        return False
      
# OR 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        FOUND_TARGET_ROW = False
        bot_r, top_r = 0, ROWS - 1
        
        while bot_r <= top_r:
            mid = (bot_r + top_r) // 2
            if target > matrix[mid][-1]:
                bot_r = mid + 1
            elif target < matrix[mid][0]:
                top_r = mid - 1
            else:
                FOUND_TARGET_ROW = True
                target_row = mid
                break

        if not FOUND_TARGET_ROW:
            return False

        left, right = 0, COLS - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[target_row][mid]:
                left = mid + 1
            elif target < matrix[target_row][mid]:
                right = mid - 1
            else:
               return True 

        return False

