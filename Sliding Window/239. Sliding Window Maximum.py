#https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        r,l = 0,0
        q = collections.deque()
        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            if r+1 >= k:
                out.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l+=1
            r+=1
        return out
