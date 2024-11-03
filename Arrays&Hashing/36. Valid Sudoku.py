#https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, column, square = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                el = board[r][c]
                if el == '.':
                    continue
                
                if (el in row[r] or el in column[c] or el in square[r//3,c//3]):
                    return (False)
                
                row[r].add(el)
                column[c].add(el)
                square[r//3,c//3].add(el)
                
        return True
            