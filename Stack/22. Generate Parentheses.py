#https://leetcode.com/problems/generate-parentheses/description/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(openp,closed,s):
            if closed == n:
                res.append(s)
                return 
                
            if openp < n: 
                dfs(openp+1, closed, s + '(')
            if closed < openp: 
                dfs(openp, closed+1, s + ')')

        res = []
        dfs(0,0,'')
        return res
