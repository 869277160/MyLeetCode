#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_speed = 1
        max_speed = max(piles)
        
        while min_speed < max_speed:

            current_speed = min_speed + (max_speed - min_speed) // 2 
            # print(min_speed, current_speed, max_speed)
            # print(self.f(piles, current_speed))
            if self.f(piles, current_speed) < h:
                # 能够在规定时间内吃完，说明现在速度过快，需要在(min_speed, mid_speed)
                max_speed = current_speed
            elif self.f(piles, current_speed) > h:
                # 不能够在规定时间内吃完，说明现在速度过慢，需要在(mid_speed, max_speed)
                min_speed = current_speed + 1
            elif self.f(piles, current_speed) == h:
                # 能够吃完，但是不一定是边界条件，说明右侧边界已经确定，需要缩小对应范围
                max_speed = current_speed
            # print(min_speed, max_speed)
            
        return min_speed 

    def f(self, piles: List[int], speed: int) -> int:
        from math import ceil
        hour = 0
        for pile in piles:
            hour += ceil(pile / speed)
        return hour 

# @lc code=end

