#
# @lc app=leetcode.cn id=2525 lang=python3
#
# [2525] 根据规则将箱子分类
#

# @lc code=start
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        Bulky = (length >= 10000 or width >= 10000 or height >= 10000) or (length*width*height >= 1000000000) 
        Heavy = mass >= 100
        
        if Bulky and Heavy:
            return "Both"
        elif Bulky and not Heavy:
            return "Bulky"
        elif Heavy and not Bulky:
            return "Heavy"
        else:
            return "Neither"
        
        
        
        
# @lc code=end

