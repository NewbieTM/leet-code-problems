#https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count = [0] * 26
        for el in s1:
            count[ord(el) - ord('a')] += 1

        windCount = [0] * 26
        for r in range(len(s2)):
            if s2[r] not in s1:
                l = r + 1
                windCount = [0] * 26
                continue

            windCount[ord(s2[r]) - ord('a')] +=1

            if r - l + 1 == len(s1):
                if windCount == count:
                    return True
                windCount[ord(s2[l]) - ord('a')] -=1
                l+=1
                
        return False

#OR Better approach by Neet
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        ds1, ds2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            ds1[ord(s1[i]) - ord('a')] +=1
            ds2[ord(s2[i]) - ord('a')] +=1

        matches = 0
        l = 0
        for i in range(26):
            matches += (1 if ds1[i] == ds2[i] else 0)

        for r in range(len(s1), len(s2)):
            
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            ds2[index] +=1
            if ds2[index] == ds1[index]:
                matches +=1
            elif ds2[index] - 1 == ds1[index]:
                matches -=1
            
            index = ord(s2[l]) - ord('a')
            ds2[index] -=1
            if ds2[index] == ds1[index]:
                matches +=1
            elif ds2[index] + 1 == ds1[index]:
                matches -=1
            l+=1
        return matches == 26
