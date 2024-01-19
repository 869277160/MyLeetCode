#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] 强整数
#

# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        # import math 
        
        res = []
        for i in range(20):
            for j in range(20):
                num = x**i + y**j
                if num <= bound and num not in res:
                    res.append(num)
        
        return res
        
        
        
# @lc code=end

