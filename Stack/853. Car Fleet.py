#https://leetcode.com/problems/car-fleet/description/
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        positions = [(p,s) for p,s in zip(position, speed)]
        positions.sort()
        for pos, spd in positions[::-1]:
            time_need = (target - pos) / spd
            if not stack or stack[-1] < time_need:
                stack.append(time_need)
            
        return len(stack)
