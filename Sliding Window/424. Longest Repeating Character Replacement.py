#https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        alphaDict = {}
        res = 0

        for r in range(len(s)):
            alphaDict[s[r]] = 1 + alphaDict.get(s[r],0)

            while (r-l + 1) - max(alphaDict.values()) > k:
                alphaDict[s[l]] -= 1
                l+=1

            res = max(res, r-l + 1)

        return res

