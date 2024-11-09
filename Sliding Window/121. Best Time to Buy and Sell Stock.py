#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_p = 0
        while r < len(prices):
            max_p = max(max_p, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r +=1
            
        return max_p
