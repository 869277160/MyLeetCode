#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            res = int(str(-x)[::-1])*(-1)
            if -2**31<res<2**31-1:
                    return res
        if x > 0:
            res = int(str(x)[::-1])
            if -2**31<res<2**31-1:
                    return res
        
        return 0
        
        
# @lc code=end

