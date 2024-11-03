#https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        basket = [[] for i in range(len(nums) + 1)]
        h = {}
        
        for el in nums:
            h[el] = 1 + h.get(el,0)
        
        for key,v in h.items():
            basket[v].append(key)
            
        
        res = []
        for b in basket[::-1]:
            for el in b:
                res.append(el)
                if len(res) == k:
                    return (res)