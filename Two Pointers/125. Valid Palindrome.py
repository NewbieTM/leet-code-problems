#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l+=1
            while not s[r].isalnum() and r > l:
                r-=1
        
            if s[l] != s[r]:
                return (False)
            l+=1
            r-=1
            
        return(True)
            
