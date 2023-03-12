#
# @lc app=leetcode.cn id=2119 lang=python3
#
# [2119] 反转两次的数字
#

# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        if num == 0 :
            return True
        elif num %10 == 0:
            return False
        else:
            return True
# @lc code=end

