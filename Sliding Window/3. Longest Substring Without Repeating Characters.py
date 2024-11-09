#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, strs: str) -> int:
        l, res = 0, 0
        charSet = set()
        for r in range(len(strs)):
            while strs[r] in charSet:
                charSet.remove(strs[l])
                l+=1
            charSet.add(strs[r])
            res = max(res, r - l + 1)

        return res
