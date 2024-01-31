#
# @lc app=leetcode.cn id=2739 lang=python3
#
# [2739] 总行驶距离
#

# @lc code=start
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # print(mainTank, additionalTank)
        if mainTank < 5:
            return mainTank * 10
        if mainTank >= 5:
            current_main = mainTank - 4 if additionalTank > 0 else mainTank - 5
            current_add = additionalTank - 1 if additionalTank > 0 else 0 
            return 50 + self.distanceTraveled(current_main, current_add)
            
        
        
# @lc code=end

