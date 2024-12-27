#https://leetcode.com/problems/koko-eating-bananas/description/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        #res = float('inf')
        while left <= right:
            mid = (left + right) // 2
            count_of_act = sum([ceil(el / mid) for el in piles]) 

            if count_of_act > h:
                left = mid + 1
            elif count_of_act <= h:
                right = mid - 1
                #res = min(res, mid)
        
        return left #return res

            
