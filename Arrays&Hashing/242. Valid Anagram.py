#https://leetcode.com/problems/valid-anagram/
class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
        hs, ht = {}, {}
        for a,b in zip(s,t):
            hs[a] = 1 + hs.get(a,0)
            ht[b] = 1 + ht.get(b,0)
        return hs == ht and len(s) == len(t)