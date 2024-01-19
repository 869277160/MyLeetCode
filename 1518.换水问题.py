#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        res = numBottles
        left = numBottles
        while left >= numExchange:
            left = numBottles // numExchange + numBottles % numExchange
            res += numBottles // numExchange
            numBottles =  left

        return res 
# @lc code=end

